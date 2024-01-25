document.addEventListener('DOMContentLoaded', function () {
    const documentos = document.querySelectorAll('.documento');

    documentos.forEach(documento => {
        documento.addEventListener('click', function () {
            const codiceDocumento = this.getAttribute('data-codice');
            window.location.href = `/visualizza/${codiceDocumento}/${this.getAttribute('data-documento')}`;
        });
    });
});

function estraiNumeroCapitolo(daStringa) {
    var match = daStringa.match(/\bCapitolo (\d+)\b/);
    return match ? parseInt(match[1]) : null;
}

function calcolaNumeroPagina(numeroCapitolo, capitoliPerPagina = 21) {
    return Math.ceil(numeroCapitolo / capitoliPerPagina);
}

function tornaAllaHomepageConPaginaCorrente(cartella, capitolo) {
    var nCapitolo = estraiNumeroCapitolo(capitolo)+1;
    page = calcolaNumeroPagina(nCapitolo);
    var nuovaURL = '/'+cartella+'?pagina=' + page;
    window.location.href = nuovaURL;
}


