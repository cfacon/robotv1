<!DOCTYPE html> <html> <head>
    <title>Sonar - sample code from morzel.net blog post</title>
    <style>
        body {
            font-size: 10px;
            font-family: Verdana;
        }
        table {
            border-collapse: collapse;
            width: 410px;
            margin-top: 5px;
            margin-bottom: 5px;
        }
        th {
            border: 1px solid #555;
            background-color: #555;
            color: white;
            padding: 2px;
            font-weight: normal;
        }
        td {
            border: 1px solid #999;
            padding: 2px;
        }
            td:nth-child(-n+2) {
                color: red;
            }
    </style> </head> <body>
    <div>
        <canvas id="sonarImage" width="410" height="210"></canvas>
        <table>
            <thead>
                <tr>
                    <th>Angle</th>
                    <th>Distance (cm)</th>
                    <th>Messages</th>
                    <th>Samples</th>
                    <th>Elapsed s</th>
                    <th>Messages/s</th>
                    <th>Samples/s</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td id="angle">n/a</td>
                    <td id="distance">n/a</td>
                    <td id="numberOfMessages">n/a</td>
                    <td id="numberOfSamples">n/a</td>
                    <td id="elapsedSeconds">n/a</td>
                    <td id="messagesPerSecond">n/a</td>
                    <td id="samplesPerSecond">n/a</td>
                </tr>
            </tbody>
        </table>
    </div>
	<ul id="eventList"><li>item 0</li></ul>
    <script src="assets/jquery-1.6.4.js"></script>
    <script src="assets/sonarStats.js"></script>
    <script src="assets/sonarImage.js"></script>
    <script src="assets/sonarConnection.js"></script>
    <script>
        $(function () {
		
            canvas = document.getElementById('sonarImage');
            context = canvas.getContext('2d');
	
            sonarImage.init('sonarImage',image);

			
    var i = 0;
      var increase = true;
	  
var source = new EventSource('/sonar/'); 

source.addEventListener("distance", function (event) {
	var newElement = document.createElement("li");
  newElement.innerHTML = "message: " + event.data;
  eventList.appendChild(newElement);
	
    });
    source.addEventListener("close", function (event) {
    source.close();
    });
 
source.onerror = function(e) {
	//alert("EventSource failed."+e);
 	var newElement = document.createElement("li");
  newElement.innerHTML = "error--: ";
  eventList.appendChild(newElement);
  
  evtSource.close();
};

	
        });
    </script> </body> </html>
