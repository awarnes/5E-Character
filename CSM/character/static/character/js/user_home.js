/**
 * Created by alexanderwarnes on 3/7/17.
 */

$(document).ready(function(evt){

    $.get('/user/characters/names/', function(data){
        for (var i=0;i<data.characters.length;i++) {
            var $char;
            $char = $('<li>').addClass('list-group-item text-center');
            $char.text(data.characters[i][0]);
            $char.on('click', function(){
                get_char($(this))
            })
            $char.appendTo($('#characters'));
        }
    });

    function get_char($text) {
        var $query = $text.text();

        $('#output').modal('toggle');

        $.get('/user/characters/specific_one/', {query_char: $query}, function(data){

            var $char = data[0]

            $('#name').text($char.char_name);
            $('#level').text($char.get_char_level);
            $('#class').text($char.char_classes.name);
            $('#race').text($char.char_race);
            $('#STR').text($char.STR_score);
            $('#DEX').text($char.DEX_score);
            $('#CON').text($char.CON_score);
            $('#INT').text($char.INT_score);
            $('#WIS').text($char.WIS_score);
            $('#CHA').text($char.CHA_score);

            $('#description').text($char.description);

            $('#features').text($char.features);
        });
    };

    $('#go').on('click', function (evt){

        var $name = $('#name').text().toLowerCase();
        var $user = $('#username').text()

        $.ajax({
            url: '/'+$user+'/characters/'+$name+'/',
            type: 'GET',
            success: function(resp){
                window.location.href = '/'+$user+'/characters/'+$name+'/'
            },
            error: function(err){
                alert("Sorry, we couldn't find your character!");
            },
        });

    });

});

