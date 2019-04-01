<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		
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
				outputEl.innerHTML	= '<b>Result:</b>' + joystick.deltaX() +' '+joystick.deltaY()
					+ (joystick.right()	? ' right'	: '')
					+ (joystick.up()	? ' up'		: '')
					+ (joystick.left()	? ' left'	: '')
					+ (joystick.down()	? ' down'       : '')	

				dir =  (joystick.right()     ? 'right'      : '')
                                        + (joystick.up()        ? 'up'         : '')
                                        + (joystick.left()      ? 'left'       : '')
                                        + (joystick.down()      ? 'down'       : '')

				// test ici si la dir a changé avant d'envoyer

if(joystick.deltaX() == 0 && joystick.deltaY() == 0)
{
dir = 'stop'
				outputEl.innerHTML	= '<b>Stop</b> '
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
