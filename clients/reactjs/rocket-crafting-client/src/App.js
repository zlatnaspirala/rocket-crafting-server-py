import React from 'react';
import './App.css';
import {notify} from './pure-components/notify';
import {Net} from './networking/net';
import {RocketMenu, RocketSmallMenu} from './components/menu';
import {RocketRegister} from './components/register';
import {RocketRegisterConfirm} from './components/confirmation';
import {RocketLogin} from './components/login';
import {RocketLoginFast} from './components/fastlogin';
import {RocketLogout} from './components/logout';

class App extends React.Component {

  constructor() {
    super()
    this.state = {
      showForms: false,
      registerVisible: false,
      registerConfirmVisible: false,
      loginVisible: false,
      loginFastVisible: false,
      logoutVisible: false,
    };
  }

  net = new Net()

  componentDidMount() {
    console.info('RocketCrafting main App component loaded.', this.net)
  }

  hideForms = () => {
    this.setState({showForms: false})
  }

  showForms = () => {
    notify.show("RocketCraftingServer Routes desc")
    this.setState({showForms: true})
  }

  showRegister = (e) => {
    this.setState({registerVisible: e})
  }

  showRegisterConfirm = (e) => {
    this.setState({registerConfirmVisible: e})
  }

  showLogin = (e) => {
    this.setState({loginVisible: e})
  }

  showLoginFast = (e) => {
    this.setState({loginFastVisible: e})
  }

  showLogout = (e) => {
    this.setState({logoutVisible: e})
  }

  render() {
    return (
      <div className="App textStroke">
        <div id="msgBox" className="msg-box animate1" onClick={notify.copy()}></div>
        <RocketSmallMenu hideForms={this.hideForms}
          showForms={this.showForms} ></RocketSmallMenu>
        <header className="App-header">
          {this.state.showForms === false ?
            <>
              <div className="textStroke" style={{width: "350px"}}>
                RocketCraftingServer Web Client examples<br />
                <img style={{width: "90px"}} src="./assets/logo5.png" alt="logo" />
                <br />
                MIT Licence
                Nikola Lukic zlatnaspirala@gmail.com
                maximumroulette.com 2024
                <RocketMenu
                  net={this.net}
                  hideForms={this.hideForms}
                  showForms={this.showForms}
                  showRegister={this.showRegister}
                  showLoginFast={this.showLoginFast}
                  showRegisterConfirm={this.showRegisterConfirm}
                  showLogin={this.showLogin}
                  showLogout={this.showLogout} ></RocketMenu>
              </div>
            </> :
            <div style={{marginTop: "50px"}}>
              {this.state.registerVisible === true ? <RocketRegister></RocketRegister> : null}
              {this.state.registerConfirmVisible === true ? <RocketRegisterConfirm></RocketRegisterConfirm> : null}
              {this.state.loginVisible === true ? <RocketLogin net={this.net} ></RocketLogin> : null}
              {this.state.loginFastVisible === true ? <RocketLoginFast></RocketLoginFast> : null}
              {this.state.logoutVisible === true ? <RocketLogout></RocketLogout> : null}
            </div>
          }
        </header>
      </div>
    )
  }
}

export default App;