$(document).ready(function(){
    $("#entryBlock").hide();
    $("td a").click(function(){
        $("#entryBlock").animate({width:'show'},350);
    }
  );
});
$(document).ready(function(){
    $("#hideButton").click(function(){
        $("#entryBlock").animate({width:'toggle'},350);
    }
  );
});
