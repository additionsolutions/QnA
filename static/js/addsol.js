$(document).ready(function(){ 
    $.get('/c/content/notice', function(data){
               $('#notice').html(data);
           });
           
    $.get('/t/etest/testlist', function(data){
               $('#tests').html(data);
           });
           
    $.get('/c/content/portion', function(data){
               $('#portion').html(data);
           });
    
    $.get('/c/content/activities', function(data){
               $('#activities').html(data);
           });
           
    $.get('/m/messaging/messaging', function(data){
               $('#messages').html(data);
           });
    
    $('#start').click(function(){
        var test_action;
	
        action = $(this).attr("test-action");
	// alert(action);
        $.get('/t/etest/sr/' + action, function(data){
                    // alert(data);
                   $('#test_area').html(data);
                   $('#start').hide();
               });
    });

});


function navigate(test_action)
{
    if(test_action == 0)
    {
	alert("Test Submitted Successfully");
    }
    var scriptUrl = "/t/etest/sr/" + test_action;
    var msg=getURL(scriptUrl);
    $('#test_area').html(msg);
}


// Record Marks
function marks( ans )
{
    //example use
    
    var scriptUrl = "/t/etest/ans/" + ans;
    var msg=getURL(scriptUrl);
    $('#ans_area').html(msg);
 
}



function getURL(url){
    return $.ajax({
        type: "GET",
        url: url,
        cache: false,
        async: false
    }).responseText;
}


