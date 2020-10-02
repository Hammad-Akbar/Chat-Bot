    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [number, setNumber] = React.useState(0);
    
    function newNumber() {
        React.useEffect(() => {
            Socket.on('number received', (data) => {
                console.log("Received number from server: " + data['number']);
                setNumber(data['number']);
            })
        });
    }
    
    newNumber();

    return (
        <div>
            <h1>Random number!</h1>
            <span>{number}</span>
            <Button />
        </div>
    );
}
