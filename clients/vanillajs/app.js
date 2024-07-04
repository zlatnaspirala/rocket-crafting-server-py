/**
 * RCS PY SOCK
 * Programming languages: Python , MongoDB , JavaScript
 * Web client part
 *  - How to use account session data with websockets
 */
var byId = function(i) {return document.getElementById(i)}
byId('logout').addEventListener("click", () => {
  // CONFIRMATION
  var data = {
    action: "LOGOUT",
    userLoginData: {
      token: byId('tokenFLogin').value,
      email: byId('emailFLogin').value
    }
  };
  socket.send(JSON.stringify(data));
})
byId('fastLogin').addEventListener("click", () => {
  // CONFIRMATION
  var data = {
    action: "FASTLOGIN",
    userLoginData: {
      token: byId('tokenFLogin').value,
      email: byId('emailFLogin').value
    }
  };
  socket.send(JSON.stringify(data));
})
byId('login').addEventListener("click", () => {
  // CONFIRMATION
  var data = {
    action: "LOGIN",
    userLoginData: {
      password: byId('passwordLogin').value,
      email: byId('emailLogin').value
    }
  };
  socket.send(JSON.stringify(data));
})
byId('registerConfirmation').addEventListener("click", () => {
  // CONFIRMATION
  var data = {
    action: "CONFIRMATION",
    userRegData: {
      token: byId('tokenConfirm').value,
      email: byId('emailConfirm').value
    }
  };
  socket.send(JSON.stringify(data));
})
byId('register').addEventListener("click", () => {
  var data = {
    action: "REGISTER",
    userRegData: {
      password: byId('password').value,
      email: byId('email').value
    }
  };
  socket.send(JSON.stringify(data));
})
const socket = new WebSocket('ws://localhost:8000');
socket.addEventListener('open', function(event) {
  socket.send('Connection Established');
});

socket.addEventListener('close', function(event) {
  console.log("ON CLOSE:" + event);
});

socket.addEventListener('message', function(event) {
  console.log("ON MESSAGE:" + event.data);
  return false;
});

socket.onmessage = function(event) {
  event.preventDefault()
  console.log("ON MESSAGE2:" + event.data);
  var item = document.createElement('p')
  item.value += event.data;
  byId('logs').value += "\n" + event.data;
  var test = JSON.parse(event.data)
  if(typeof test.rocketStatus != 'undefined') {
    alert("rocketStatus : " + test.rocketStatus)
    if (test.rocketStatus === "USER_LOGGED") {
      for (var item in test.flag) {
        notify.show(item + ":" + test.flag[item])
      }
    }
  } else {
    alert(test)
  }
  return false;
};