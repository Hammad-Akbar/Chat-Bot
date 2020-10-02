import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let random = Math.floor(Math.random() * 100);
    console.log('Generated a random number: ', random);
    
    Socket.emit('new number', {
        'number': random,
    });
    
    console.log('Sent a random number ' + random + ' to server!');

    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit}>
            <button>Send up a random number!</button>
        </form>
    );
}
