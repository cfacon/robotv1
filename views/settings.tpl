<!doctype html>
<HTML lang="fr">
  <HEAD>
     <TITLE>{{title}}</TITLE>
     <meta charset="UTF-8">
<link rel="stylesheet" href="assets/pure-release-1.0.0/pure-min.css">
<link rel="stylesheet" href="assets/fontawesome/css/all.css">
<link rel="stylesheet" href="assets/global.css">
<meta name="viewport" content="width=device-width, initial-scale=1">  
</HEAD>
  <body>

<div class="container">
    <span class="right"><a class="pure-button pure-button-primary" onclick="restart()">Restart</a></span>
    <span class="right"><a class="pure-button pure-button-primary" onclick="shutdown()">Shutdown</a></span>
    
    <form method='post' action='settings' class="pure-form pure-form-aligned">
  <fieldset>
<legend>Config</legend>
        <div class="pure-control-group">
            <label for="vitesse">vitesse</label>
            <input name="vitesse" id="vitesse" class="pure-input-1" type="text" placeholder="XX" value={{!vitesse}}>
        </div>
      




  </fieldset>
    <span class="left"><input type='submit' value='save' class="pure-button pure-button-primary"/></span>
    <span class="right"><a class="pure-button pure-button-primary" href="/">Retour</a></span>

</form>
</div>

<script>
function ajaxRequest(url, callback = function(){}) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      callback(xhr);
    };
    xhr.open("GET", url, true);
    xhr.send(null);
  }

function restart()
{
    var r = confirm("restart ?");
  if (r == true) {
	ajaxRequest("/cmd/restart", function(xhr){})
  }
}
function shutdown()
{
    var r = confirm("shutdown ?");
  if (r == true) {
	ajaxRequest("/cmd/shutdown", function(xhr){})
  }
}
    </script>
  </body>
</html>
