from django.test import TestCase

# Create your tests here.
<script>
    function deleteMineral(id) {
        if (id) {
          $('#mineralId').val(id);
          $('#deleteModal').modal('show');
        } else {
          console.error('ID no válido:', id);
        }
    }

    $(document).ready(function() {
        function deleteMineral(id) {
          $('#mineralId').val(id);
          $('#deleteModal').modal('show');
        }
      
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
    });

</script>