function allow() {}
function login() {
  var name = document.getElementById('name');
  var password = document.getElementById('password');
  if (name === "A Person") {
    if (password ==='pass') {
      allow('A person')
    }
  }
}
