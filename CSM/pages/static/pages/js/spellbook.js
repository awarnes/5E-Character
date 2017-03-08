/**
 * Created by alexanderwarnes on 3/7/17.
 */

$(document).ready(function(evt){

    $('.list-group-item').on('click', function(evt){
        var $query = $(this).text();

        $('#output').modal('toggle');

        $.get('/spells/spell_info/', {spell: $query}, function(data){

            $('#name').text(data.name);
            $('#level').text(data.level);
            $('#school').text(data.school);
            $('#cast_time').text(data.cast_time);
            $('#distance').text(data.distance);
            $('#components').text(data.raw_materials);
            $('#duration').text(data.duration);

            if (data.concentration === true) {
                $('#concentration').text('Yes');
            } else {
                $('#concentration').text('No');
            }

            if (data.ritual === true) {
                $('#ritual').text('Yes');
            } else {
                $('#ritual').text('No');
            }

            $('#description').text(data.description);
            $('#available_to').text(data.available_to);
        });
    })


})

