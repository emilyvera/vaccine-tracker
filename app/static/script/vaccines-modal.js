$(document).ready(function () {
    $('#submit-vaccine').click(function () {
        const vID = $('#vaccine-modal').find('.form-control1').val()
        const round_of_dose = $('#vaccine-modal').find('.form-control2').val()
        const vaccine_type = $('#vaccine-modal').find('.form-control3').val()
           $.ajax({
            type: 'POST',
            url: '/create_vaccine/' + vID + '/' + round_of_dose + '/' + vaccine_type,
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

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete_vaccine/' + encodeURIComponent(remove.data('content')),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.edit').click(function () {
        const state = $(this)
        const vID = state.data('source')


        $('#edit').click(function () {
            const type = $('#vaccine-modal2').find('.form-control3').val()

	        $.ajax({
	            type: 'POST',
	            url: '/edit_vaccine/' + vID,
	            contentType: 'application/json;charset=UTF-8',
	            data: JSON.stringify({
	                'type': type
	            }),
	            success: function (res) {
	                console.log(res)
	                location.reload();
	            },
	            error: function () {
	                console.log('Error');
	            }
	        });
	    });
	});
	$('#search').click(function () {
        const vID = $('#vaccine-modal3').find('.form-control1').val()

        $.ajax({
            type: 'POST',
            url: '/search_vaccine/' + vID,
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log(res)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.all').click(function () {
        $.ajax({
            type: 'GET',
            url: '/vaccines' ,
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

    $('.query').click(function () {
        $.ajax({
            type: 'POST',
            url: '/query_vaccine' ,
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