$(document).ready(function(){ 
    $.get('/c/content/notice', function(data){
               $('#notice').html(data);
           });
           
    $.get('/p/ptest/examlist', function(data){
               $('#exam').html(data);
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
    
    $.get('/c/content/photo', function(data){
               $('#photo_gallary').html(data);
           });
    
    $('#start').click(function(){
        //var test_action;
        action = $(this).attr("test-action");
        $.get('/t/etest/sr/' + action, function(data){
                   $('#test_area').html(data);
                   $('#start').hide();
               });
    });
    
    $('#pstart').click(function(){
        //var test_action;
        action = $(this).attr("test-action");
        $.get('/p/ptest/sr/' + action, function(data){
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

function pnavigate(test_action)
{
    if(test_action == 0)
    {
        alert("Test Submitted Successfully");
    }
    var scriptUrl = "/p/ptest/sr/" + test_action;
    var msg=getURL(scriptUrl);
    $('#test_area').html(msg);
}

// Record Marks
function marks( ans )
{
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

function recordMarks() {
    var cnt = document.forms["QForm"]["count"].value;
    loopcount = cnt + 1

    for (i = 1; i < loopcount; i++) { 
        //var x = document.forms["QForm"][i].value;
        var ans = document.getElementById("q"+[i]).value
        var scriptUrl = "/p/ptest/recoans/" + ans;
        var msg=getURL(scriptUrl);
        // write answer to db 
    }
    if (ans == null || ans == "") {
        alert("No Answer given");
        return false;
    }
}

