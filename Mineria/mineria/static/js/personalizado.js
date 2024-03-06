
//FUNCION PARA LOS FORMULARIO DE FORMULARIO DE APP DE TRANSPORTE 
document.getElementById('transporteForm').addEventListener('submit', function() {
    var errorMessages = document.getElementsByClassName('error-message');
    for (var i = 0; i < errorMessages.length; i++) {
        errorMessages[i].style.display = 'block';
    }
});
//FUNCION DLE AJAX PARA EL MODEL DE VER INFORMACION
function loadMineralDetails(id) {
    $.ajax({
        url: '/mineria/load_mineral_details/',
        data: {
            'id': id
        },
        dataType: 'json',
        success: function (data) {
            $('.modal-body').html('<p>Nombre: ' + data.nombre + '</p><p>Lugar de extracción: ' + data.lugar_extraccion + '</p><p>Peso: ' + data.peso + '</p><p>Pureza: ' + data.pureza + '</p>');
        }
    });
}
/*
//FUNCION PARA ELIMINAR EN EL UN MINERAL DE LA LISTA DE MINERALES

function deleteMineral(id) {
    if (id) {
      $('#mineralId').val(id);
      $('#deleteModal').modal('show');
    }
}

// AGREGANDO EL CONTROLADOR DE EVENTOS DE BOTON DE ELIMINAR 


$(document).ready(function() {
    $('#deleteForm').on('submit', function(e) {
      e.preventDefault();
      var id = $('#mineralId').val();  
      $.ajax({
        url: '/mineria/delete_mineral/',
        data: {
          'id': id
        },
        dataType: 'json',
        success: function (data) {
          if (data.success) {
            $('#deleteModal').modal('hide');
            location.reload(true); 
          }
        }
      });
    });
}); */
