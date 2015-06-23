$(document).ready(function(){ 
    $.get('/c/content/notice', function(data){
               $('#notice').html(data);
           });
           
    $.get('/t/etest/testlist', function(data){
               $('#tests').html(data);
           });
    
    $('#start').click(function(){
        var test_action;
        action = $(this).attr("test-action");
        $.get('/t/etest/sr/' + action, function(data){
                   // alert(data);
                   $('#test_area').html(data);
                   $('#start').hide();
               });
    });

});


function admin_nav(action)
{
    alert(action);
}

// Code for Summary report
function getSummary()
{
	var usrid = document.getElementById("usrSelect").value;
	// alert (usrid);
	$.get('/a/dmin/summary/'+ usrid, function(data){
		$('#summaryreport').html(data);
	});
}

// Code for User report
function getResult()
{
	var usrid = document.getElementById("usrSelect").value;
	var testid = document.getElementById("testSelect").value;
	//alert (usrid);
	//alert (testid);
	$.get('/a/dmin/scorecard/' + usrid + '/' + testid, function(data){
               $('#userreport').html(data);
           });
}

// Code for list of Tessetline
function gettestsetLine()
{
	var testid = document.getElementById("testSelect").value;
	// alert(testid);
	$.get('/a/dmin/testsetlinedisplay/' + testid, function(data){
               $('#testsetlinearea').html(data);
           });
}

// Code for list of Content
function getContentlist()
{
	var ctype_id = document.getElementById("contentTypeSelect").value;
	// alert(ctype_id);
	
	$.get('/a/dmin/contentdisplay/' + ctype_id, function(data){
               $('#contentarea').html(data);
           });
}

function getOption()
{
	var question_id = document.getElementById("questionSelect").value;
	//alert ("Hello");
	$.get('/a/dmin/optiondisplay/' + question_id, function(data){
               $('#optionarea').html(data);
           });
}

// Record Marks
function marks( ans )
{
    //example use
    //alert(ans);
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



