import * as React from 'react';
import GoogleLogin from 'react-google-login';
import Socket from './Socket';

const handleSubmit = (response) => {
  const { name } = response.profileObj;
  Socket.emit('new google user', {
    name,
  });
};

const handleSubmitFailure = () => {
  const name = 'Guest';
  Socket.emit('new google user', {
    name,
  });
};

export default function GoogleButton() {
  return (
    <GoogleLogin
      clientId="914224010125-bp302rh7fisq3v0hd29ts701abv851jr.apps.googleusercontent.com"
      buttonText="Login"
      onSuccess={handleSubmit}
      onFailure={handleSubmitFailure}
      cookiePolicy="single_host_origin"
    />
  );
}
