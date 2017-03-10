/**
 * Created by alexanderwarnes on 3/7/17.
 */

$(document).ready(function(evt){

    $('.list-group-item').on('click', function(evt){
        var $query = $(this).text();

        $('#output').modal('toggle');

        $.get('/spells/spell/', {query_spell: $query}, function(data){

            $('#name').text(data[0].name);
            $('#level').text(data[0].level);
            $('#school').text(data[0].school);
            $('#cast_time').text(data[0].cast_time);
            $('#distance').text(data[0].distance);
            $('#components').text(data[0].raw_materials);
            $('#duration').text(data[0].duration);

            if (data[0].concentration === true) {
                $('#concentration').text('Yes');
            } else {
                $('#concentration').text('No');
            }

            if (data[0].ritual === true) {
                $('#ritual').text('Yes');
            } else {
                $('#ritual').text('No');
            }

            $('#description').text(data[0].description);
            $('#available_to').text(data[0].available_to);
        });
    })


})

