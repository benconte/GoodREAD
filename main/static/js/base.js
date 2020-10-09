 setTimeout(function(){
  $(".loader_bg").fadeToggle();
 });

 var comment_reply = document.getElementById('comment-reply');
 var comment_respond = document.getElementById('comment-response');

 function inputFieldDisplay(){
 	comment_respond.style.display = "all";
 }