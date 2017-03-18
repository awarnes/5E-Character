/**
 * Created by alexanderwarnes on 3/17/17.
 */

$(document).ready(function(){

    $('.list-group-item').on('click', function (evt){

        var $query = $(this).data('slug');
        var $type = $(this).data('type')

        $('#output').modal('toggle');

        $.get('/api/v1/' + $type + $query, function (data){
            $('#name').text(data.name);
            $('#description').text(data.description);
            $('#name').data('slug', data.slug);

        })
    });

    $('#open_details').on('click', function(evt){
        var $type = 'features';
        var $slug = $('#name').data('slug')
        window.location.href= '/' + $type + '/details/' + $slug + '/'

    });

    $('#table').on('click', function(evt){
        $('#table_img').slideToggle();
    })

    $('#feature_container').on('dblclick', function(evt){
        $('#features').slideToggle()
    })

    $('#property_container').on('dblclick', function(evt){
        $('#properties').slideToggle()
    })

});