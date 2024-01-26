from flask import Flask, request, render_template
import os
from waitress import serve
import re

app = Flask(__name__)

@app.context_processor
def handle_context():
    return dict(os=os)

def ordina_elementi(elementi):
    def estrai_numero(elemento):
        match = re.search(r'\d+', elemento)
        return int(match.group()) if match else 0

    return sorted(elementi, key=estrai_numero)

def trova_precedente_successivo(array, elemento):
    indice_elemento = array.index(elemento) if elemento in array else -1

    precedente = array[indice_elemento - 1] if indice_elemento > 0 else None
    successivo = array[indice_elemento + 1] if indice_elemento < len(array) - 1 else None

    return precedente, successivo


# Specifica il numero di elementi da visualizzare per pagina
n = 21

@app.route('/')
@app.route('/<cartella>')
def index(cartella=None):
    # Specificare il codice della cartella
    cartella = 'onepiece' if cartella is None else cartella
    # Trovare tutte le sottocartelle
    cartelle_documenti = [d for d in os.listdir(os.path.join('static', 'documents', cartella)) if os.path.isdir(os.path.join('static', 'documents', cartella, d))]
    cartelle_documenti = ordina_elementi(cartelle_documenti)
    # Ottenere il numero di pagina dalla query string, con default a 1 se non specificato
    pagina_corrente = int(request.args.get('pagina', 1))
    # Calcola l'indice di inizio e fine per la pagina corrente
    inizio = (pagina_corrente - 1) * n
    fine = pagina_corrente * n
    # Estrarre solo gli elementi per la pagina corrente
    cartelle_pagina_corrente = cartelle_documenti[inizio:fine]
    # Calcolare il numero totale di pagine necessarie
    numero_pagine_totali = (len(cartelle_documenti) + n - 1) // n
    return render_template('/index.html', cartella=cartella, cartelle_pagina_corrente=cartelle_pagina_corrente, numero_pagine_totali=numero_pagine_totali, pagina_corrente=pagina_corrente)

@app.route('/visualizza/<cartella>/<capitolo>')
def visualizza_documento(cartella, capitolo):
    folder_path = os.path.join('static', 'documents', cartella, capitolo)
    # Cerco il documento precedente e successivo
    cartelle_documenti = [d for d in os.listdir(os.path.join('static', 'documents', cartella)) if os.path.isdir(os.path.join('static', 'documents', cartella, d))]
    cartelle_documenti = ordina_elementi(cartelle_documenti)
    precedente, successivo = trova_precedente_successivo(cartelle_documenti, capitolo)
    # Calcola il numero di pagina attuale
    indice = cartelle_documenti.index(capitolo) if capitolo in cartelle_documenti else -1
    pagina = indice // n + 1
    # Elencare i file nella cartella del capitolo e filtrare solo quelli che sono file e terminano con '.jpg' o '.png'
    lista_pagine = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and (f.lower().endswith('.jpg') or f.lower().endswith('.png'))]
    # Ottenere il numero di pagine dal conteggio della lunghezza della lista
    numero_pagine = len(lista_pagine)
    return render_template('visualizza.html', cartella=cartella, capitolo=capitolo, lista_pagine=lista_pagine, numero_pagine=numero_pagine, precedente=precedente, successivo=successivo, pagina=pagina)

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    #app.run(host='0.0.0.0', port=5000, debug=True)

