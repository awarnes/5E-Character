/**
 * Created by alexanderwarnes on 3/16/17.
 */


$(document).ready(function(){

    $('.search_term').on('click', function (evt){

        var $query = $(this).text();

        var $type = $(this).attr('data-type').toLowerCase();

        $('#output').modal('toggle');

        // $type = $type.substring(0, ($type.length - 1));

        const $equipment = ['weapons', 'armors', 'items', 'tools'];

        if ($type === 'spells') {
            $.get('/spells/spell/'+$query, {query_spell: $query}, function (data){
                $('#name').text(data[0].name)
                $('#description').text(data[0].description)
            })
        }   else if ($equipment.indexOf($type) != -1) {
            $.get('/search/weapon',{query: $query}, function (data){
                $('#name').text(data[0].name)
                $('#description').text(data[0].description)
            })
        }  else {
            $.get('/api/v1/rules/'+$type, function (data){
                $('#name').text(data)
                $('#description').text(data)
            })
        }


    })

})