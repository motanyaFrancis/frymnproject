$(window).load(function () {

    $('#medicineSelect').on('change', function() {
        let medicineValue = this.value;

       $.ajax({
            url: '/activities/orders/get_company_list',
            data: {
              'medicinevalue': medicineValue,
            },
            dataType: 'html',
            success: function (data) {
                $('#collegeSelect').html(data);
            }
          });

    });

});