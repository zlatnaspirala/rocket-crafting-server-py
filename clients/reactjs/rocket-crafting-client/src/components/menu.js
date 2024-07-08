import React from 'react';

export class RocketMenu extends React.Component {

  registerRef = React.createRef();
  registerConfirmRef = React.createRef();
  loginRef = React.createRef();
  fastLoginRef = React.createRef();
  logoutRef = React.createRef();

  constructor(props) {
    super()
    this.showForms = () => {
      props.showRegister(this.registerRef.current.checked)
      props.showRegisterConfirm(this.registerConfirmRef.current.checked)
      props.showLogin(this.loginRef.current.checked)
      props.showLoginFast(this.fastLoginRef.current.checked)
      props.showLogout(this.logoutRef.current.checked)
      props.showForms()
    }
  }

  empty () {}

  componentDidMount() {
    console.log('RocketCrafting Menu components loaded.')
  }

  render() {
    return (
      <div style={{display: "flex", flexDirection: "column", zIndex:2}}>
        <h2>Select form</h2>
        <label>
          <input ref={this.registerRef} type="checkbox" onChange={this.empty} />
          Register
        </label>
        <label>
          <input ref={this.registerConfirmRef} type="checkbox" onChange={this.empty} />
          Register Confirm
        </label>
        <label>
          <input ref={this.loginRef} type="checkbox" onChange={this.empty} />
          Login
        </label>
        <label>
          <input ref={this.fastLoginRef} type="checkbox" onChange={this.empty} />
          Fast Login
        </label>
        <label>
          <input ref={this.logoutRef} type="checkbox" onChange={this.empty} />
          Logout
        </label>

        <label>
          <button onClick={this.showForms}>OK</button>
        </label>
      </div>
    );
  }
}

export class RocketSmallMenu extends React.Component {
  constructor(а) {
    super()
  }

  showMenu = () => {
    this.props.hideForms()
  }

  render() {
    return (
      <div style={{display: "flex", flexDirection: "column", position: "absolute", left: "0", width: "150px"}}>
        <button style={{width: "100%", height: "fit-content"}} onClick={this.showMenu} className=''>
          <div data-text="Menu" className="textStroke">Menu</div>
        </button>
      </div>)
  }
}
