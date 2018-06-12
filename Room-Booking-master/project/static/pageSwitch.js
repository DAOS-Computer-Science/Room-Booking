$(document).ready(function(){
    $("#entryBlock").css("height", $("#mainTable").height());
});
$(window).on('resize', function(){
    $("#entryBlock").css("height", $("#mainTable").height());
});
$(document).ready(function(){
    $("#entryBlock").hide();
    $("td a").click(function(){
        $("#entryBlock").animate({width:'show',opacity:1},350);
    }
  );
});
$(document).ready(function(){
    $("#hideButton").click(function(){
        $("#entryBlock").animate({width:'toggle'},350);
    }
  );
});
