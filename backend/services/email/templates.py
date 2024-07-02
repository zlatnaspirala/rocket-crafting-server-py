
def confirmationTemplate(token, userName):
    return """<!doctype html>
      <html xmlns="http://www.w3.org/1999/xhtml"> 
        <head> 
          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
          <meta name="viewport" content="width=device-width" />
        </head>
        <body>
          <div style="background:linear-gradient(45deg, #ff6900, #d80000);color:white;height: 550px;font-size: large;padding: 20px;">
          <h3> Welcome to GamePlay Platform,<br /> 
            dear <span style="color: black" > """ + userName + """</span>. </h3><br/>
          <p>Confirm you email address: <br/>
            Copy/Paste in your SignUp form.</p> <br/>
          <p>CODE: """ + token + """ </p> <br /><br /><br />
          <small>Based on Safir and RocketCraftingServer projects.</small>
          <img style="width:80px;" src="https://github.com/zlatnaspirala/safir/blob/main/hello/assets/icons/192.png?raw=true"/>
          <small>Get source code at https://github.com/zlatnaspirala<small>
          <small>Powered by maximumroulette.com 2024</small>
        </div>
        </body>
        </html>"""


def getConfirmationForgotPass(token, userName):
    return """<div style='background:linear-gradient(45deg, #ff6900, #d80000);color:white;font-size: large;padding: 20px;'>
      <h2> - RocketCraftingServer platform - </h2> 
      Forgot Password confirmation email. <br/>
      <h3>Dear {userName}. </h3><br/>
      <p>You will need this CODE to confirm your new password: <br/>
      Copy/Paste in your Forgot password form.</p> <br/>
      CODE : <h2>{token}</h2>  <br/><br/><br/>
      <small>RocketCraftingServer py server project.</small>
      <small>Get source code at https://github.com/zlatnaspirala<small>
      <small>Powered by maximumroulette.com 2024</small>
      <br/>
      </div>"""
