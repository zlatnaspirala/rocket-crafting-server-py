import {notify} from '../pure-components/notify';
import React from 'react';

export class RocketLogin extends React.Component {

  refEmailLogin = React.createRef();
  refPasswordLogin = React.createRef();

  constructor(arg) {
    super()
    console.log("arg", arg.net.socket.send)
  }

  componentDidMount() {
    console.log('RocketCrafting RocketLogin componets loaded.')
  }

  login = () => {
    notify.show("LOGIN")
    var data = {
      action: "LOGIN",
      userLoginData: {
        password: this.refPasswordLogin.current.value,
        email: this.refEmailLogin.current.value
      }
    }
    this.props.net.socket.send(JSON.stringify(data))
  }

  non() {}

  render() {
    return (
      <div className="myForms">
        <h3>LOGIN FORM</h3>
        <input onChange={(e) => this.non(e)} ref={this.refEmailLogin} type="email" />
        <input onChange={(e) => this.non(e)} ref={this.refPasswordLogin} type="password" />
        <button onClick={this.login} >Login</button>
      </div>
    );
  }
}
