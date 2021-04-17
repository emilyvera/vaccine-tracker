$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#deaths-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const cityId = button.data('source') // Extract info from data-* attributes
        const date = button.data('content') // Extract info from data-* attributes

        const modal = $(this)
        // if (cityId === 'New Death') {
        //     modal.find('.modal-title').text(cityId)
        //     $('#deaths-form-display').removeAttr('cityId')
        // } else {
        //     modal.find('.modal-title').text('Edit Death ' + cityId)
        //     $('#deaths-form-display').attr('cityId', cityId)
        // }

        if (date) {
            modal.find('.form-control').val(date);
        } else {
            modal.find('.form-control').val('');
        }
    })


    $('#submit-death').click(function () {
        const cID = $('#deaths-modal').find('.form-control1').val()
        const date = $('#deaths-modal').find('.form-control2').val()
        const numDeaths = $('#deaths-modal').find('.form-control3').val()

        $.ajax({
            type: 'POST',
            url: '/create_death/' + cID + '/' + encodeURIComponent(date) + '/' + numDeaths,
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
            url: '/delete_death/' + encodeURIComponent(remove.data('source')) + '/' + remove.data('content'),
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
            const numDeaths = $('#deaths-modal2').find('.form-control3').val()

            $.ajax({
                type: 'POST',
                url: '/edit_death/' + cID + '/' + encodeURIComponent(date),
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'num_deaths': numDeaths
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
        const cID = $('#deaths-modal3').find('.form-control1').val()
        const date = $('#deaths-modal3').find('.form-control2').val()

        $.ajax({
            type: 'POST',
            url: '/search_death/' + cID + '/' + encodeURIComponent(date),
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
            url: '/deaths' ,
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
            url: '/query_death' ,
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