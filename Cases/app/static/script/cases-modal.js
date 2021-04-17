$(document).ready(function () {

    $('#submit-case').click(function () {
        const cID = $('#cases-modal').find('.form-control1').val()
        const date = $('#cases-modal').find('.form-control2').val()
        const numCases = $('#cases-modal').find('.form-control3').val()

        $.ajax({
            type: 'POST',
            url: '/create_case/' + cID + '/' + encodeURIComponent(date) + '/' + numCases,
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
            url: '/delete_case/' + encodeURIComponent(remove.data('source')) + '/' + remove.data('content'),
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

        $('#edit').click(function () {
            const numCases = $('#cases-modal2').find('.form-control3').val()

            $.ajax({
                type: 'POST',
                url: '/edit_case/' + cID + '/' + encodeURIComponent(date),
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'num_cases': numCases
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
        const cID = $('#cases-modal3').find('.form-control1').val()
        const date = $('#cases-modal3').find('.form-control2').val()

        $.ajax({
            type: 'POST',
            url: '/search_case/' + cID + '/' + encodeURIComponent(date),
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
            url: '/cases' ,
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
            url: '/query_case' ,
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