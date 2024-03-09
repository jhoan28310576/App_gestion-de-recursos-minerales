
//FUNCION PARA LOS FORMULARIO DE FORMULARIO DE APP DE TRANSPORTE 
document.getElementById('transporteForm').addEventListener('submit', function() {
    var errorMessages = document.getElementsByClassName('error-message');
    for (var i = 0; i < errorMessages.length; i++) {
        errorMessages[i].style.display = 'block';
    }
});