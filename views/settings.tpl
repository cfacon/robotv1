<!doctype html>
<HTML lang="fr">
  <HEAD>
     <TITLE>{{title}}</TITLE>
     <meta charset="UTF-8">
     <link rel="stylesheet" href="https://unpkg.com/purecss@1.0.0/build/pure-min.css" integrity="sha384-nn4HPE8lTHyVtfCBi5yW9d20FjT8BJwUXyWZT9InLYax14RDjBj46LmSztkmNP9w" crossorigin="anonymous">
<meta name="viewport" content="width=device-width, initial-scale=1">  
</HEAD>
 
  <body>
<a href="/">retour</a>



    <form method='post' action='settings' class="pure-form  pure-form-aligned">
  <fieldset>
    <legend>GPIO</legend>

	<div class="pure-control-group">
            <label for="moteur1_enA">moteur1_enA</label>
            <input name="moteur1_enA" id="moteur1_enA" type="text" placeholder="XX" value={{!moteur1_enA}}>
        </div>
        <div class="pure-control-group">
            <label for="moteur1_en1">moteur1_en1</label>
            <input name="moteur1_en1"Ã id="moteur1_en1" type="text" placeholder="XX" value={{!moteur1_en1}}>
        </div>
        <div class="pure-control-group">
            <label for="moteur1_en2">moteur1_en2</label>
            <input name="moteur1_en2" id="moteur1_en2" type="text" placeholder="XX" value={{!moteur1_en2}}>
        </div>


  </fieldset>
    <input type='submit' value='save' class="pure-button pure-button-primary"/>
</form>

  </body>
</html>
