import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newAddress = document.getElementById("address_input").value;
    Socket.emit('new address input', {
        'address': newAddress,
    });
    
    console.log('Sent the address ' + newAddress + ' to server!');

    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit}>
            <input id="address_input" placeholder="Enter an address"></input>
            <button>Add to DB!</button>
        </form>
    );
}
