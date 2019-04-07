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
    <form method='post' action='settings' class="pure-form pure-form-aligned">
  <fieldset>
<legend>GPIO moteur 1</legend>
        <div class="pure-control-group">
            <label for="moteur1_enA">enA</label>
            <input name="moteur1_enA" id="moteur1_enA" class="pure-input-1-4" type="text" placeholder="XX" value={{!moteur1_enA}}>
        </div>
        <div class="pure-control-group">
            <label for="moteur1_en1">en1</label>
            <input name="moteur1_en1" id="moteur1_en1" class="pure-input-1-4" type="text" placeholder="XX" value={{!moteur1_en1}}>
        </div>
        <div class="pure-control-group">
            <label for="moteur1_en2">en2</label>
            <input name="moteur1_en2" id="moteur1_en2" class="pure-input-1-4" type="text" placeholder="XX" value={{!moteur1_en2}}>
        </div>
<legend>GPIO moteur 2</legend>
        <div class="pure-control-group">
            <label for="moteur2_enA">enB</label>
            <input name="moteur2_enA" id="moteur2_enA" class="pure-input-1-4" type="text" placeholder="XX" value={{!moteur2_enB}}>
        </div>
        <div class="pure-control-group">
            <label for="moteur2_en1">en1</label>
            <input name="moteur2_en1" id="moteur2_en1" class="pure-input-1-4" type="text" placeholder="XX" value={{!moteur2_en1}}>
        </div>
        <div class="pure-control-group">
            <label for="moteur2_en2">en2</label>
            <input name="moteur2_en2" id="moteur2_en2" class="pure-input-1-4" type="text" placeholder="XX" value={{!moteur2_en2}}>
        </div>


  </fieldset>
    <span class="left"><input type='submit' value='save' class="pure-button pure-button-primary"/></span>
 <span class="right"><a class="pure-button pure-button-primary" href="/">Retour</a></span>

</form>
</div>


  </body>
</html>
