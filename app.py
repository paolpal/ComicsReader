from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Specificare il codice della cartella
    codice_cartella = 'onepiece'

    # Trovare tutte le sottocartelle
    cartelle_documenti = [d for d in os.listdir(os.path.join('static', 'documents', codice_cartella)) if os.path.isdir(os.path.join('static', 'documents', codice_cartella, d))]

    # Ottenere il numero di pagina dalla query string, con default a 1 se non specificato
    pagina_corrente = int(request.args.get('pagina', 1))

    # Specifica il numero di elementi da visualizzare per pagina
    n = 21

    # Calcola l'indice di inizio e fine per la pagina corrente
    inizio = (pagina_corrente - 1) * n
    fine = pagina_corrente * n

    # Estrarre solo gli elementi per la pagina corrente
    cartelle_pagina_corrente = cartelle_documenti[inizio:fine]

    # Calcolare il numero totale di pagine necessarie
    numero_pagine_totali = (len(cartelle_documenti) + n - 1) // n

    return render_template('/index.html', codice_cartella=codice_cartella, cartelle_pagina_corrente=cartelle_pagina_corrente, numero_pagine_totali=numero_pagine_totali, pagina_corrente=pagina_corrente)

@app.route('/visualizza/<codice_cartella>/<documento>')
def visualizza_documento(codice_cartella, documento):
    folder_path = os.path.join('static', 'documents', codice_cartella, documento)
    # Elencare i file nella cartella e filtrare solo quelli che sono file e terminano con '.jpg'
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.jpg')]
    # Ottenere il numero di pagine dal conteggio della lunghezza della lista
    numero_pagine = len(file_list)
    return render_template('visualizza.html', codice_cartella=codice_cartella, documento=documento, numero_pagine=numero_pagine)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

