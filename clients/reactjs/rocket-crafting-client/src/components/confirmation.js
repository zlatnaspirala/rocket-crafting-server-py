import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketRegister extends React.Component {

  constructor(arg) {
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
      <div className="myForms">
        <div className="myForms">
            <h3>REGISTER FORM</h3>
            <div style={{ margin: "5px 5px 5px 5px", padding: "5px 5px 5px 5px", border: "solid 1px black"}}>
                <label>Detail:</label>
                <textarea onChange={(e) => this.non(e)} value='var data = { action: "REGISTER", userRegData: { password: byId("password").value, email: byId("email").value }}; socket.send(JSON.stringify(data));' >
                </textarea>
            </div>
            <input  onChange={(e) => this.non(e)}  id="email" type="email" value="zlatnaspirala@gmail.com" />
            <input  onChange={(e) => this.non(e)}  id="password" type="password" value="123123123" />
            <button onClick={this.register} id="register">Register test</button>
        </div>

        <div className="myForms">
          <h3>REGISTER CONFIRMATION FORM</h3>
          <input  onChange={(e) => this.non(e)} id="emailConfirm" type="email" value="zlatnaspirala@gmail.com" />
          <input  onChange={(e) => this.non(e)} id="tokenConfirm" type="password" value="" />
          <button id="registerConfirmation">Confirm</button>
        </div>
        <div className="myForms">
          <h3>LOGIN FORM</h3>
          <input  onChange={(e) => this.non(e)} id="emailLogin" type="email" value="zlatnaspirala@gmail.com" />
          <input  onChange={(e) => this.non(e)} id="passwordLogin" type="password" value="" />
          <button id="login">Login</button>
        </div>
        <div className="myForms">
          <h3>FAST LOGIN FORM</h3>
          <input  onChange={(e) => this.non(e)} id="emailFLogin" type="email" value="zlatnaspirala@gmail.com" />
          <input  onChange={(e) => this.non(e)} id="tokenFLogin" type="password" value="" />
          <button id="fastLogin">Fast Login</button>
        </div>
        <div className="myForms">
          <h3>LOGOUT FORM</h3>
          <input  onChange={(e) => this.non(e)} id="emailLogout" type="email" value="zlatnaspirala@gmail.com" />
          <input  onChange={(e) => this.non(e)} id="tokenLogout" type="password" value="" />
          <button id="logout">Logout</button>
        </div>

      </div>
    );
  }
}

export class AccountComponent extends RocketRegister {
  render() {
    return (
      <div>
        {super.render()}
      </div>
    );
  }
}