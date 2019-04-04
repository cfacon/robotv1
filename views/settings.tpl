<!doctype html>
<HTML lang="fr">
  <HEAD>
     <TITLE>{{title}}</TITLE>
     <meta charset="UTF-8">
  </HEAD>
 
  <body>
<a href="/">retour</a>



    <form method='post' action='settings'>
  <fieldset>

    <legend>GPIO</legend>
    <p>
      <input type='text' name='moteur1_enA' placeholder='votre ip' value={{!moteur1_enA}} />
      <label for="moteur1_enA">moteur1_enA</label>
    </p>
  </fieldset>
    <input type='submit' value='ok'/>
</form>

  </body>
</html>
