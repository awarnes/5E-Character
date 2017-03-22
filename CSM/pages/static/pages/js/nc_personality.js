$(document).ready(function(){

    var $alignment = $('#id_alignment');

    $("#id_alignment>option:last-of-type").remove();

    $alignment.on('change', function(){
        var $alignment_query = $('#id_alignment option:selected').text().toLowerCase();
        var re = /\s/

        $alignment_query = $alignment_query.replace(re, '-');

        if ($alignment_query !== '---------') {
            $.get('/api/v1/rules/alignments/' + $alignment_query, function(data){
                $('#alignment_name').text(data.name);
                $('#alignment_desc').text(data.description);
                $('#alignemnt_examples').text(data.examples);
            });
        } else {
            $('#alignment_name').empty();
            $('#alignment_desc').empty();
            $('#alignemnt_examples').empty();
        }
    });


});