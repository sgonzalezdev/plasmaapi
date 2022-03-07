/*
Global Js
 -Title: PlasmaAPI
 -Details: Scope JS on thi file is applied across all applications.  
 -Version: 0.1.0
 -Autor: Sergio Enmanuel González
 
 */

//Getting the button properties.
btn_up = document.getElementById("btn-up");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    btn_up.style.display = "block";
  } else {
    btn_up.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function btnScrollTop() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
