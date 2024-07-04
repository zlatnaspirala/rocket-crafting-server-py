import React from 'react';
import './App.css';
import {AccountComponent} from "./components/account";
import {notify} from './pure-components/notify';
import {Net} from './networking/net';

class App extends React.Component {

  net = new Net()
  componentDidMount() {
    console.log('RocketCrafting Account componets loaded.' , this.net)
  }

  render() {
    return (
      <div className="App">
        <div id="msgBox" className="msg-box animate1" onClick={notify.copy()}></div>
        <header className="App-header">
          <img className="App-logo" alt="Powered by RocketCraftingServer" src="assets/rocket-craft.png"></img>
          <AccountComponent></AccountComponent>
        </header>
      </div>
    )
  }
}

export default App;