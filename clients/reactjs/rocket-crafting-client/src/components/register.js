import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketRegister extends React.Component {

  constructor(arg) {
    super()
    console.log("arg", arg)
  }
  componentDidMount() {
    console.log('RocketCrafting Account componets loaded.')
  }

  register() {
    notify.show("REGISTER CALL")
    console.log('RocketCrafting Account register call.')

  }

  non() {
    // console.log("non")
  }

  render() {
    return (
      <div className="myForms gradient-background">
        <h3>REGISTER FORM</h3>
        <div style={{margin: "5px 5px 5px 5px", padding: "5px 5px 5px 5px", border: "solid 1px black"}}>
          <label>Detail:</label>
          <textarea onChange={(e) => this.non(e)} value='var data = { action: "REGISTER", userRegData: { password: byId("password").value, email: byId("email").value }}; socket.send(JSON.stringify(data));' >
          </textarea>
        </div>
        <input onChange={(e) => this.non(e)} id="email" type="email" value="zlatnaspirala@gmail.com" />
        <input onChange={(e) => this.non(e)} id="password" type="password" value="123123123" />
        <button onClick={this.register} id="register">Register test</button>
      </div>
    );
  }
}

// export class RegisterComponent extends RocketRegister {
//   render() {
//     return (
//       <div>
//         {super.render()}
//       </div>
//     );
//   }
// }