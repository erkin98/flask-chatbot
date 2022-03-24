// import { Button } from "@material-ui/core";
import React from "react";
import "./Login.css";
function Login() {

  return (
    <div className="login">
      <img
        className="login__logo"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/897px-WhatsApp.svg.png"
        alt=""
      />
      <div className="login__text">
        <h1>Sign in to WhatsApp</h1>
      </div>
      {/* <Button type="submit" onClick={signIn}>
        Sign in with Google
      </Button> */}
    </div>
  );
}

export default Login;
