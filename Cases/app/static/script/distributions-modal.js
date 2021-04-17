$(document).ready(function () {

    $('#submit-distribution').click(function () {
        const cID = $('#distribution-modal').find('.form-control1').val()
        const date = $('#distribution-modal').find('.form-control2').val()
        const num_delivered = $('#distribution-modal').find('.form-control3').val()
        const type_param= $('#distribution-modal').find('.form-control4').val()
        $.ajax({
            type: 'POST',
            url: '/create_distribution/' + cID + '/' + encodeURIComponent(date) + '/' + num_delivered + '/' + encodeURIComponent(type_param),
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
            url: '/delete_distribution/' + encodeURIComponent(remove.data('source')) + '/' + remove.data('content') + '/' + remove.data('content2') ,
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
        const cID = state.data('source')
        const date = state.data('content')
        const type_param = state.data('content2')

        $('#edit').click(function () {
            const numDelivered = $('#distribution-modal2').find('.form-control3').val()

            $.ajax({
                type: 'POST',
                url: '/edit_distribution/' + cID + '/' + encodeURIComponent(date) + '/'+ encodeURIComponent(type_param),
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'num_delivered': numDelivered
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
        const cID = $('#distribution-modal3').find('.form-control1').val()
        const date = $('#distribution-modal3').find('.form-control2').val()
        const type_param = $('#distribution-modal3').find('.form-control3').val()

        $.ajax({
            type: 'POST',
            url: '/search_distribution/' + cID + '/' + encodeURIComponent(date)+ '/' + encodeURIComponent(type_param),
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
            url: '/distributions' ,
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
            url: '/query_distribution' ,
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