$(document).ready(function () {
   


    $('#safety').click(function () {
        
        $.ajax({
            type: 'POST',
            url: '/safety',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});