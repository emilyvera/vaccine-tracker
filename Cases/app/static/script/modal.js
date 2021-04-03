$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#cases-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const cityId = button.data('source') // Extract info from data-* attributes
        const date = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        if (cityId === 'New Case') {
            modal.find('.modal-title').text(cityId)
            $('#cases-form-display').removeAttr('cityId')
        } else {
            modal.find('.modal-title').text('Edit Case ' + cityId)
            $('#cases-form-display').attr('cityId', cityId)
        }

        if (date) {
            modal.find('.form-control').val(date);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-case').click(function () {
        const cID = $('#cases-modal').find('.form-control1').val()
        const date = $('#cases-modal').find('.form-control2').val()
        const numCases = $('#cases-modal').find('.form-control3').val()

        $.ajax({
            type: 'POST',
            url: '/create/' + cID + '/' + encodeURIComponent(date) + '/' + numCases,
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
            url: '/delete/' + encodeURIComponent(remove.data('source')) + '/' + remove.data('content'),
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
                url: '/edit/' + cID + '/' + encodeURIComponent(date),
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
            url: '/search/' + cID + '/' + encodeURIComponent(date),
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
            url: '/' ,
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