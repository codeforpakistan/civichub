const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

$(document).ready(function(){
  
})


function likeThis(e, icon) {
  $(e).children().first().toggleClass(`bi-${icon}`).toggleClass(`bi-${icon}-fill`);
  // e.firstElementChild.classList.remove('bi-heart');
  // e.firstElementChild.classList.toggle('bi-heart-fill');
}