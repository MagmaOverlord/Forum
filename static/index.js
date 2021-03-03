function send(endpoint) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", endpoint);

  

  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({
    "name": $("#name").val(),
    "subject": $("#subject").val(),
    "post": $("#para").val()
  }));
}