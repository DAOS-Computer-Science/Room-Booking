var allow = function(title,forename,surname) {
document.getElementsByName('title').selectedIndex = title;
document.getElementsByName('firstName').value = forename;
document.getElementsByName('surname').value = surname;
}

var login = function() {
  var name = document.getElementById('name');
  var password = document.getElementById('password');

  if (name === "A Person" && password ==='pass') {
    allow('Mr','A','Person');
  }
}
