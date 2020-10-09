    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [messagees, setMessagees] = React.useState([]);
    
    function getNewMessagees() {
        React.useEffect(() => {
            Socket.on('messagees received', (data) => {
                console.log("Received messagees from server: " + data['allmessagees']);
                setMessagees(data['allmessagees']);
            })
        });
    }
    
    getNewMessagees();

    return (
        <div>
            <h1>Welcome to the chatroom!</h1>
                <ol>
                    {
                        messagees.map(
                            (message, index) =>
                                <li key={index}> {message} </li>
                        )
                    }
                </ol>
            <Button />
        </div>
    );
}
