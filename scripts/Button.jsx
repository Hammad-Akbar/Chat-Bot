import * as React from 'react';
import Socket from './Socket';

function handleSubmit(event) {
  const newMessage = document.getElementById('message_input');
  Socket.emit('new message input', {
    message: newMessage.value,
  });

  newMessage.value = '';

  event.preventDefault();
}

export default function Button() {
  return (
    <form onSubmit={handleSubmit}>
      <input id="message_input" placeholder="Enter a message:" />
      <button type="submit">Send</button>
    </form>
  );
}
