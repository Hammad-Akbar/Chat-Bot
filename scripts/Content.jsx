import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';
import { GoogleButton } from './GoogleButton';
import './Content.css';

function check(message) {
    if (message.startsWith(" ")) {
        return message;
    }
    else {
        message = null;
        return message
    }
}

function checkNot(message) {
    if (message.startsWith(" ") == false) {
        return message;
    }
    else if (message.startsWith("!! ")) {
        return message;
    }
    else {
        message = null;
        return message;
    }
}

export function Content() {
    const [messages, setMessages] = React.useState([]);
    const [accounts, setAccounts] = React.useState([]);
    
    function getNewMessages() {
        
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                console.log("Received messages from server: " + data['allmessages']);
                setMessages(data['allmessages']);
            })
        });
    }
    
    getNewMessages();
    
    function getAllAccounts() {
        React.useEffect(() => {
            Socket.on('accounts received', (data) => {
                let allAccounts = data['allAccounts'];
                console.log("Received accounts from server: " + allAccounts);
                setAccounts(allAccounts);
            })
        });
    }
    
    getAllAccounts();
    
    const bot = "BOT";
    
    function getUserName() {
        let user = "GUEST";
        accounts.map((account, index) =>
            <li key={index}> {account} </li>
        );
        return user
    }

    return (
        <div className="App">
            <GoogleButton />
            <div className="App-header">
              <h1>Welcome to the Chatroom!</h1>
            </div>
                <ol>
                    {
                        messages.map((message, index) =>
                            <li key={index}> 
                                <div className="messageSent"> <div className="userName"> {getUserName().toUpperCase()}</div> <div className="message"><p> {checkNot(message)} </p></div></div>
                                <div className="botMessage"> <div className="botName"> {bot.toUpperCase()} </div> <div className="message"><p>{check(message)}</p></div> </div>
                            </li>
                        )
                    }
                    
                </ol>
            <Button />
        </div>
    );
}