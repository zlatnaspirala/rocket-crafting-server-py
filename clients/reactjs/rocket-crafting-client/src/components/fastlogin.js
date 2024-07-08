import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketLoginFast extends React.Component {

  constructor(arg) {
    super()
  }

  componentDidMount() {
    console.log('RocketCrafting Account componets loaded.')
  }

  fastLogin() {
    notify.show("fastLogin CALL")
  }

  non() {}

  render() {
    return (
      <div className="myForms">
        <h3>FAST LOGIN FORM</h3>
        <input onChange={(e) => this.non(e)} id="emailFLogin" type="email" value="zlatnaspirala@gmail.com" />
        <input onChange={(e) => this.non(e)} id="tokenFLogin" type="password" value="" />
        <button id="fastLogin" onClick={this.fastLogin}> Fast Login</button>
      </div>
    );
  }
}
