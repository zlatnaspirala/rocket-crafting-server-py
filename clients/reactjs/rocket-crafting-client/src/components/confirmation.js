import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketRegisterConfirm extends React.Component {

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
      <div className="myForms gradient-background textColors1">
        <h3>REGISTER CONFIRMATION FORM</h3>
        <input onChange={(e) => this.non(e)} id="emailConfirm" type="email" value="zlatnaspirala@gmail.com" />
        <input onChange={(e) => this.non(e)} id="tokenConfirm" type="password" value="" />
        <button id="registerConfirmation">Confirm</button>
      </div>
    );
  }
}
