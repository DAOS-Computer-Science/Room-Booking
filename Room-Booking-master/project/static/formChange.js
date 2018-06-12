$(document).ready(function(){
  $("td a").click(function(){
    var classes = $(this).attr("class");
    var classes = classes.split(" ");
    var roomList = ["K5","K6","K7"];
    var days = ["monday","tuesday","wednesday","thursday","friday"];
    var times = ["registration","p1","p2","p3","lunch","p4","p5","afterSchool"];
    var bodyID = $("body").attr("id");


    for (i=0;i<(days.length);i++){
      if (classes[0] == days[i]) {
        //$('#day').val(days[i]);
		$('#day0').val(days[i]);
      }
      else {}
    };
    for (i=0;i<(times.length);i++){
      if (classes[1] == times[i]) {
        //$('#time').val(times[i]);
		$('#time0').val(times[i]);
      }
      else {}
    };
    for (i=0;i<(roomList.length);i++){
      if (bodyID == roomList[i]) {
        //$('#room').val(roomList[i]);
		$('#room0').val(roomList[i]);
      }
      else {}
    };
  })
})
