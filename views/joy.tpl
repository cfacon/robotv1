<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		<link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">		
		<meta name="viewport" content="width=device-width, initial-scale=1">		
<style>
		#container {
			width		: 100%;
			height		: 100%;
			overflow	: hidden;
			padding		: 0;
			margin		: 0;
			-webkit-user-select	: none;
			-moz-user-select	: none;
		}
		</style>
	</head>
	<body>
		<div id="info">
			<span><a href="/settings">settings</a></span>
			<span id="result"></span>
		</div>
		<div id="container"></div>

                <script type="text/javascript" src="/assets/virtualjoystick.js/virtualjoystick.js"></script>
		<script>

function ajaxRequest(url, callback = function(){}) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      callback(xhr);
    };
    xhr.open("GET", url, true);
    xhr.send(null);
  }
			var dirG = ''

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
				var outputEl	= document.getElementById('result');
				outputEl.innerHTML = '<b>start</b> '
			})
			joystick.addEventListener('touchEnd', function(){
				var outputEl	= document.getElementById('result');
				outputEl.innerHTML = '<b>stop</b> '
this.dirG = 'stop'
ajaxRequest("/cmd/"+dirG, function(xhr){})


			})

			setInterval(function(){

				var outputEl	= document.getElementById('result');


		if( joystick.right() ){
			outputEl.innerHTML	= '<b>Result: right</b>'
			dir = 'right'
		}
		if( joystick.left() ){
			outputEl.innerHTML	= '<b>Result: left</b>'
			dir = 'left'
		}
		if( joystick.up() ){
			outputEl.innerHTML	= '<b>Result: up</b>'
			dir = 'up'
		}
		if( joystick.down() ){
			outputEl.innerHTML	= '<b>Result: down</b>'
			dir = 'down'
		}

if(joystick.deltaX() == 0 && joystick.deltaY() == 0)
{
dir = 'stop'
}

if (dirG != dir)
{
this.dirG = dir;                                
ajaxRequest("/cmd/"+dirG, function(xhr){})
}

			}, 1/30 * 100);
		</script>
	</body>
</html>
