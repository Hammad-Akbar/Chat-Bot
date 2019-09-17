import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
    handleSubmit(event) {
        event.preventDefault();
    
        // this is a local variable so we don't need to initialize in the constructor
        let random = Math.floor(Math.random() * 100);
        console.log('Generated a random number: ', random);
        Socket.emit('new number', {
            'number': random,
        });
        console.log('Sent a random number to server!');
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <button>Send up a random number!</button>
            </form>
        );
    }
}