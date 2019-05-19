<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		<link rel="stylesheet" href="assets/pure-release-1.0.0/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
		<link rel="stylesheet" href="assets/fontawesome/css/all.css" crossorigin="anonymous">
		<link rel="stylesheet" href="assets/global.css">
		<meta name="viewport" content="width=device-width, initial-scale=1">		
	</head>
	<body>
		<div id="info" class="leftright">
<span class="left">
<a class="pure-button" href="/settings">
    <i class="fa fa-cog"></i> </a> 
<button class="pure-button fas fa-stop" onclick="stop()"> stop</button>

</span>
<span class="right" id="result"></span>
<span class="right" id="resultmouse">--</span>
</div>
		<div id="container"></div>

                <script type="text/javascript" src="/assets/virtualjoystick.js/virtualjoystick.js"></script>
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

var joystick	= new VirtualJoystick({
				container	: document.getElementById('container'),
				mouseSupport	: true,
				stationaryBase	: true,
				baseX		: 200,
				baseY		: 200,
				limitStickTravel: true,
				stickRadius: 50
			});

var outputEl	= document.getElementById('result');
				outputEl.innerHTML = '<b>stop button</b> '
	ajaxRequest("/cmd/1", function(xhr){})
}
			

			var joystick	= new VirtualJoystick({
				container	: document.getElementById('container'),
				mouseSupport	: true,
				stationaryBase	: true,
				baseX		: 200,
				baseY		: 200,
				limitStickTravel: true,
				stickRadius: 50
			});
			joystick.addEventListener('touchStart', function(){
				var outputEl	= document.getElementById('resultmouse');
				outputEl.innerHTML = '<b>start</b> '
			})
			joystick.addEventListener('touchEnd', function(){
				var outputEl	= document.getElementById('resultmouse');
				outputEl.innerHTML = '<b>touchEnd stop</b> '
//                this.dirG = 'stop'
                //ajaxRequest("/cmd/stop", function(xhr){})
			})
			joystick.addEventListener('mouseUp', function(){
				var outputEl	= document.getElementById('resultmouse');
				outputEl.innerHTML = '<b>mouseUp stop</b> '
                this.dirG = '1'
                ajaxRequest("/cmd/1", function(xhr){})
			})
			joystick.addEventListener('mouseDown', function(){
				var outputEl	= document.getElementById('resultmouse');
				outputEl.innerHTML = '<b>mouseUp stop</b> '
                this.dirG = '1'
                ajaxRequest("/cmd/1", function(xhr){})
			})
            

			setInterval(function(){

				var outputEl	= document.getElementById('result');

        if( joystick.right() ){
            dir = '5'
        }
        if( joystick.left() ){
            dir = '4'
        }
        if( joystick.up() ){
            dir = '2'
        }
        if( joystick.down() ){
            dir = '3'
        }
        if (dirG != dir)
        {
            isStop = 'false'

            dirG = dir;
             outputEl.innerHTML	= '<b>Result: '+ dir +'</b>'
            ajaxRequest("/cmd/"+dirG, function(xhr){})
        }

			}, 1/30 * 100);
		</script>
	</body>
</html>
