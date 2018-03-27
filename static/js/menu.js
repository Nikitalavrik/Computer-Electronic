console.log(1)
$('#block_form').submit(function(e){
    $.post('/add/', $(this).serialize(), function(data){
        $('#output').html(data.toString())
    });
    e.preventDefault();
});
