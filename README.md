# rocket-crafting-server-py

## Alias RCS-Py

## Based on webSocket tech

- New RCServer [python vs mongoDB]
- RCC/RocketCraftingClient examples [done in js and py]

## Install:

```bash
python -m venv env
source env/bin/activate

python -m pip install "pymongo[srv]"
python -m pip install python-dateutil
python -m pip install pycryptodome
```

If you have any error lof like missing module just install it.

## Documentation for websock RCS-Py

Same shema also used in visual-ts game engine && Rest api RCS variant.

- Route : `register`

```js
msgFromCLient.action === "REGISTER";
msgFromCLient.data.userRegData.email & password;
```

- Response with:

```js
 "USER_REGISTERED" or "USER_ALREADY_REGISTERED"
```

After "USER_REGISTRED" Server send validation code to the user email and sock emit data ->

```js
let codeSended = {
  action: "CHECK_EMAIL",
  data: {
    accessToken: socketId,
    text: "Please check your email to get verification code. Paste code here :",
  },
};
codeSended = JSON.stringify(codeSended);
callerInstance.userSockCollection[socketId].send(codeSended);
console.log("Email reg sended. Notify client.");
```

In error case :

```js
console.warn("Connector error in sending reg email!", error);
let codeSended = {
  action: "ERROR_EMAIL",
  data: {
    errMsg:
      "Please check your email again!, Something wrong with current email!",
  },
};
codeSended = JSON.stringify(codeSended);
callerInstance.userSockCollection[socketId].send(codeSended);
console.log("Email reg error. Notify client.");
```
