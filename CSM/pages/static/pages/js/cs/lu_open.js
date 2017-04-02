
$(document).ready(function(){
    "use strict";

    $('.search_query').on('click', function (evt){

        var $query = $(this).data('slug');
        var $name = $(this).prop('id')

        $('#output').modal('toggle');


        $.get('/api/v1/rules/classes/' + $query, function (data){
            $('#name').text(data.name);
            $('#name').data('slug', $query);
            $('#cur_level').text('Current Level: ' + $char_classes[$name]);
            $('#description').text(data.description);
        })

    });

    $('#open_details').on('click', function(evt){
            var $slug = $('#name').data('slug');
            window.location.href='/classes/details/' + $slug + '/'

    });

    $('#level_up').on('click', function(evt){
        var $slug = $('#name').data('slug');

        $.get('/level_up/'+$slug+'/', function(){
            window.location.href='/level_up/'+$slug+'/'
        })
    })

});