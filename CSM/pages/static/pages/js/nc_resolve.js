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

});