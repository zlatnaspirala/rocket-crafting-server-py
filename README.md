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

### - Route : `register`

Client request:
```js
var data = {
    action: "REGISTER",
    userRegData: {
        password: byId('password').value,
        email: byId('email').value
    }
};
socket.send(JSON.stringify(data));
```

```js
msgFromCLient.action === "REGISTER";
msgFromCLient.data.userRegData.email & password;
```

- Response with:

```js
 "USER_REGISTERED" or "USER_ALREADY_REGISTERED"
```

After "USER_REGISTRED" Server send validation code to the user email and sock emit data ->

Client request:
```js
var data = {
  action: "CONFIRMATION",
  userRegData: {
    token: byId("token").value,
    email: byId("email").value,
  },
};
socket.send(JSON.stringify(data));
```

Confirmation code response:
```js
  {"message": "Confirmation done.", "rocketStatus": "USER_CONFIRMED"}
```

