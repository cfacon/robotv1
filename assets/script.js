/*Code relative to the fullscreen api inspired from this source: http://html5professor.com/tutoriels-18.html */

function enterFullscreen(element) {
  if(element.requestFullScreen) {
    //fonction officielle du w3c
    element.requestFullScreen();
  } else if(element.webkitRequestFullScreen) {
    //fonction pour Google Chrome
    element.webkitRequestFullScreen(Element.ALLOW_KEYBOARD_INPUT);
  } else if(element.mozRequestFullScreen){
    //fonction pour Firefox
    element.mozRequestFullScreen();
  } else {
    alert('Votre navigateur ne supporte pas le mode plein écran');
  }
}

function exitFullscreen() {
  if(document.cancelFullScreen) {
    //fonction officielle du w3c
    document.cancelFullScreen();
  } else if(document.webkitCancelFullScreen) {
    //fonction pour Google Chrome
    document.webkitCancelFullScreen();
  } else if(document.mozCancelFullScreen){
    //fonction pour Firefox
    document.mozCancelFullScreen();
  }
}
