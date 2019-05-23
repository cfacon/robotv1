<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		<link rel="stylesheet" href="assets/pure-release-1.0.0/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
		<link rel="stylesheet" href="assets/fontawesome/css/all.css" crossorigin="anonymous">
		<link rel="stylesheet" href="assets/global.css">
        <link rel="stylesheet/less" type="text/css" href="assets/button.less">
        <script type="text/javascript" src="assets/less.min.js"></script>
		<meta name="viewport" content="width=device-width, initial-scale=1">		
	</head>
	<body>
		<div id="info" class="leftright">
<span class="right">
            <a class="pure-button" href="/settings">
    <i class="fa fa-cog"></i> </a> 
<button class="pure-button fas fa-stop" onclick="stop()"> stop</button>
</span>
<span class="right" id="result">**</span>
</div>
        
<span class="left">
<table>
  <tr>
<td class=""></td>
<td class="icono-arrow1-up" onclick="up()"></td>
<td class=""> </td>
  </tr>
  <tr>
<td class="icono-arrow1-right" onclick="left()"></td>
<td></td>
<td class="icono-arrow1-left" onclick="right()"></td>
  </tr>
  <tr>
<td class=""></td>
<td class="icono-arrow1-down" onclick="down()"></td>
<td class=""> </td>
  </tr>
</table>
        </span>
        
        
		<script>
var dirG = ''
var isStop = 'true'

function ajaxRequest(url, callback = function(){}) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      callback(xhr);
    };
    xhr.open("GET", url, true);
    xhr.send(null);
  }

function stop()
{
    isStop = 'true'

    var outputEl	= document.getElementById('result');
	outputEl.innerHTML = '<b>stop button</b> '
	ajaxRequest("/cmd/1", function(xhr){})
}

function left()
{
    var outputEl	= document.getElementById('result');
	outputEl.innerHTML = '<b>left button</b> '
	ajaxRequest("/cmd/7", function(xhr){})
}
function right()
{
    var outputEl	= document.getElementById('result');
	outputEl.innerHTML = '<b>right button</b> '
	ajaxRequest("/cmd/6", function(xhr){})
}
function up()
{
    var outputEl	= document.getElementById('result');
	outputEl.innerHTML = '<b>up button</b> '
	ajaxRequest("/cmd/2", function(xhr){})
}
function down()
{
    var outputEl	= document.getElementById('result');
	outputEl.innerHTML = '<b>down button</b> '
	ajaxRequest("/cmd/3", function(xhr){})
}
            
            

	
		</script>
	</body>
</html>
