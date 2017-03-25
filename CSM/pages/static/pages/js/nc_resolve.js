$(document).ready(function(){

    $(".sortable").sortable({
       connectWith: ".sortable",
       placeholder: "ui-state-highlight"
    }).disableSelection();

    $('#accept').on('click', function(){
       $('#id_next_page').val('home');
    });

    $('#delete').on('click', function(evt){
        $('#delete_check').modal('toggle');
    });

    $('#delete_yes').on('click', function(){
        $('#id_next_page').val('delete');
    });

    $('#delete_no').on('click', function(){
        $('#delete_check').modal('toggle');
    });

    $('.search_query').on('click', function (evt){

        var $query = $(this).data('slug');

        var re = /\s/g;

        var $type = $(this).data('type').toLowerCase();

        $type = $type.replace(re, '_');

        $('#output').modal('toggle');

        const $equipment = ['weapons', 'armors', 'items', 'tools'];

        if ($type === 'spells') {
            $.get('/api/v1/spells/spell/'+$query, function (data){
                $('#name').text(data.name);
                $('#name').data('type', $type);
                $('#name').data('slug', $query);
                $('#description').text(data.description);
            })
        }   else if ($equipment.indexOf($type) != -1) {
            $.get('/api/v1/equipment/' + $type + '/' + $query, function (data){
                $('#name').text(data.name);
                $('#name').data('type', $type);
                $('#name').data('slug', $query);
                $('#description').text(data.description);
            })
        }  else {
            $.get('/api/v1/rules/' + $type + '/' + $query, function (data){
                $('#name').text(data.name);
                $('#name').data('type', $type);
                $('#name').data('slug', $query);
                $('#description').text(data.description);
            })
        }


    });

    $('#open_details').on('click', function(evt){
            var $type = $('#name').data('type');
            var $slug = $('#name').data('slug')
            window.location.href='/' + $type + '/details/' + $slug + '/'

    });

    $('.search_type').on('click', function (evt){

        var $type_data = $(this).attr('data-type');

        var queries = document.getElementsByClassName('search_query');

        for (var i=0; i<queries.length; i++){
            if (queries[i].dataset.search_type === $type_data) {
                $(queries[i]).slideToggle();
            }
        }
    });
});