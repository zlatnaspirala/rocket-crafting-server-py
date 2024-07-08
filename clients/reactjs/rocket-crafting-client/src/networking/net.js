import {notify} from "../pure-components/notify";
import {byId} from "../services/utils";

export class Net {

  socket = new WebSocket('ws://localhost:8000');

  constructor() {

    this.socket.addEventListener('open', function(event) {
      this.send('Connection Established');
    });

    this.socket.addEventListener('close', function(event) {
      console.log("ON CLOSE:" + event);
    });

    // this.socket.addEventListener('message', function(event) {
    //   console.log("ON MESSAGE:" + event.data);
    //   return false;
    // });

    this.socket.onmessage = function(event) {
      event.preventDefault()
      console.log("ON MESSAGE2:" + event.data);
      var item = document.createElement('p')
      item.value += event.data;
      byId('logs').value += "\n" + event.data;
      var test = JSON.parse(event.data)
      if(typeof test.rocketStatus != 'undefined') {
        alert("rocketStatus : " + test.rocketStatus)
        if(test.rocketStatus === "USER_LOGGED") {
          for(var i in test.flag) {
            notify.show(i + ":" + test.flag[i])
          }
        }
      } else {
        alert(test)
      }
      return false;
    }
  }
}