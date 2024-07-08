import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketLogin extends React.Component {

  constructor(arg) {
    super()
    console.log("arg", arg)
  }

  componentDidMount() {
    console.log('RocketCrafting RocketLogin componets loaded.')
  }

  login() {
    notify.show("login CALL")
    console.log('RocketCrafting login call.')
  }

  non() {
    // console.log("non")
  }

  render() {
    return (
      <div className="myForms">
        <div className="myForms">
          <h3>LOGIN FORM</h3>
          <input onChange={(e) => this.non(e)} id="emailLogin" type="email" value="zlatnaspirala@gmail.com" />
          <input onChange={(e) => this.non(e)} id="passwordLogin" type="password" value="" />
          <button id="login" onClick={this.login} >Login</button>
        </div>
      </div>
    );
  }
}
