$(document).ready(function() {
    console.log("starting1")
    var site_base_url = 'http://localhost:5050';
    
    $('#loader').hide();

    // button handler for help queue
    $("#run-button").on('click', function () {
        var freshq = $("#freshman-q").prop('value');
        var sophq = $("#sophomore-q").prop('value');
        var junq = $("#junior-q").prop('value');
        var senq = $("#senior-q").prop('value');
        $('#assignments-table').empty()
        $('#loader').show();
        console.log("making request")
        $.ajax({
            type: "GET",
            url: site_base_url + "/run",
            data: 'freshman-q='+freshq+'&sophomore-q='+sophq+'&junior-q='+junq+'&senior-q='+senq
            
        }).then(function(data) {
            // console.log(data)
            console.log("getting results")
            setInterval(function() {
                $.ajax({
                    type: "GET",
                    url: site_base_url + "/get_results",
                    
                }).then(function(data) {
                    console.log(data)
                    $('#loader').hide();
                    $('#assignments-table').empty()
                        var key_render = ""
                        $('#assignments-table').append(
                            $('<tr>').append(
                                $('<td>').text(key_render),
                                $('<td>').text(data.results)
                            )
                        );
                    
                });
            }, 1000);
        });
    });
});