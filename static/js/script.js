document.addEventListener('DOMContentLoaded', function () {
    const documentos = document.querySelectorAll('.documento');

    documentos.forEach(documento => {
        documento.addEventListener('click', function () {
            const codiceDocumento = this.getAttribute('data-codice');
            window.location.href = `/visualizza/${codiceDocumento}/${this.getAttribute('data-documento')}`;
        });
    });
});
