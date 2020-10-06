    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [addresses, setAddresses] = React.useState([]);
    
    function getNewAddresses() {
        React.useEffect(() => {
            Socket.on('addresses received', (data) => {
                console.log("Received addresses from server: " + data['newAddresses']);
                setAddresses(data['newAddresses']);
            })
        });
    }
    
    getNewAddresses();

    return (
        <div>
            <h1>Addresses!</h1>
                <ol>
                    {addresses.map(address => <li>{address}</li>)}
                </ol>
            <Button />
        </div>
    );
}
