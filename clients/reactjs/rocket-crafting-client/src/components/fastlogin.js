import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketLoginFast extends React.Component {

  refEmailFLogin = React.createRef();
  refTokenFLogin = React.createRef();

  constructor(arg) {
    super()
  }

  componentDidMount() {
    console.log('RocketCrafting RocketLoginFast componets loaded.')
  }

  fastLogin = () => {
    notify.show("fastLogin CALL")
    notify.show("FASTLOGIN")
    var data = {
      action: "FASTLOGIN",
      userLoginData: {
        token: this.refTokenFLogin.current.value,
        email: this.refEmailFLogin.current.value
      }
    }
    this.props.net.socket.send(JSON.stringify(data))
  }

  non() {}

  render() {
    return (
      <div className="myForms">
        <h3>FAST-LOGIN FORM</h3>
        <input onChange={(e) => this.non(e)} ref={this.refEmailFLogin} type="email" />
        <input onChange={(e) => this.non(e)} ref={this.refTokenFLogin} type="password" />
        <button onClick={this.fastLogin}> Fast Login</button>
      </div>
    );
  }
}
