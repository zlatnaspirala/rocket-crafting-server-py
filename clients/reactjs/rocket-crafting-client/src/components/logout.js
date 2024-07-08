import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketLogout extends React.Component {

  constructor(arg) {
    super()
  }

  componentDidMount() {
    console.log('RocketCrafting Account componets loaded.')
  }

  register() {
    notify.show("REGISTER CALL")
    console.log('RocketCrafting Account register call.')
  }

  non() {}

  render() {
    return (
      <div className="myForms">
        <h3>LOGOUT FORM</h3>
        <input onChange={(e) => this.non(e)} id="emailLogout" type="email" value="zlatnaspirala@gmail.com" />
        <input onChange={(e) => this.non(e)} id="tokenLogout" type="password" value="" />
        <button id="logout">Logout</button>
      </div>
    );
  }
}