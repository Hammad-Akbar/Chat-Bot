import * as React from 'react';
import { Socket } from './Socket';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';


const handleSubmit = (response) => {
    console.log("Successfully logged in")
    let name = response.profileObj.name;
    Socket.emit('new google user', {
        'name': name,
    });
    
    console.log('Sent the name ' + name + ' to server!');
}

const handleSubmitFailure = (response) => {
  console.log("Failed to login")
   let name = "Guest";
    Socket.emit('New Guest User', {
        'Guest': name,
    });
    
    console.log('Sent the name ' + name + ' to server!');
}

export function GoogleButton() {
    return <GoogleLogin
            clientId="914224010125-bp302rh7fisq3v0hd29ts701abv851jr.apps.googleusercontent.com"
            buttonText="Login"
            onSuccess={handleSubmit}
            onFailure={handleSubmitFailure}
            cookiePolicy={'single_host_origin'}
          />;
}


