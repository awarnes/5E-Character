$(document).ready(function(){

    var $background = $('#id_background');


    $background.on('change', function(){
        var $background_query = $('#id_background option:selected').text().toLowerCase();
        var re = /\s/

        $background_query = $background_query.replace(re, '-');

        if ($background_query !== '---------') {
            $.get('/api/v1/rules/backgrounds/' + $background_query, function(data){
                $('#features').empty();
                $('#name').text(data.name);
                $('#description').text(data.description);
                $('#gold').text(data.gold_start);
                $('#special').text(data.specials);

                for (var i = 0; i < data.features.length; i++) {
                    var $feature = $('<li>', {text: data.features[i].name});
                    $('#features').append($feature);
                }

            });
        } else {
            $('#name').empty();
            $('#description').empty();
            $('#gold').empty();
            $('#features').empty();
            $('#special').empty();
        }
    });


});