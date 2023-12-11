from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Specificare il codice della cartella
    codice_cartella = 'onepiece'

    # Trovare tutte le sottocartelle
    cartelle_documenti = [d for d in os.listdir(os.path.join('static', 'documents', codice_cartella)) if os.path.isdir(os.path.join('static', 'documents', codice_cartella, d))]

    return render_template('/index.html', codice_cartella=codice_cartella, cartelle_documenti=cartelle_documenti)

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

