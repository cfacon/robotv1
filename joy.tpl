<html>
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0">
		
		<style>
		body {
			overflow	: hidden;
			padding		: 0;
			margin		: 0;
			background-color: #BBB;
		}
		#info {
			position	: absolute;
			top		: 0px;
			width		: 100%;
			padding		: 5px;
			text-align	: center;
		}
		#info a {
			color		: #66F;
			text-decoration	: none;
		}
		#info a:hover {
			text-decoration	: underline;
		}
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
		<div id="container"></div>
		<div id="info">
			<span id="result"></span>
		</div>

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

			console.log("touchscreen is", VirtualJoystick.touchScreenAvailable() ? "available" : "not available");
	
			var joystick	= new VirtualJoystick({
				container	: document.getElementById('container'),
				mouseSupport	: true,
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
				outputEl.innerHTML	= '<b>Result:</b> '
					+ ' dx:'+joystick.deltaX()
					+ ' dy:'+joystick.deltaY()
					+ (joystick.right()	? ' right'	: '')
					+ (joystick.up()	? ' up'		: '')
					+ (joystick.left()	? ' left'	: '')
					+ (joystick.down()	? ' down'       : '')	

				dir =  (joystick.right()     ? ' right'      : '')
                                        + (joystick.up()        ? ' up'         : '')
                                        + (joystick.left()      ? ' left'       : '')
                                        + (joystick.down()      ? ' down'       : '')

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
