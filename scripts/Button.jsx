import * as React from 'react';
import { Socket } from './Socket';

export function Button() {
    const handleSubmit = event => {
        let random = Math.floor(Math.random() * 100);
        console.log('Generated a random number: ', random);
        Socket.emit('new number', {
            'number': random,
        });
        console.log('Sent a random number to server!');

        event.preventDefault();
    }
    
    return (
        <form onSubmit={handleSubmit}>
            <button>Send up a random number!</button>
        </form>
    );
}
