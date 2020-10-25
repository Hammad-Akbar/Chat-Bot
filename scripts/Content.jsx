import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';
import { GoogleButton } from './GoogleButton';
import './Content.css';
import Linkify from 'react-linkify';


function check(message) {
    if (message.startsWith(" ")) {
        return 1;
    }

    else {
        return 0;
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
            Socket.on('users updated', (data) => {
                let allAccounts = data['allUsers'];
                console.log("Received accounts from server: " + allAccounts);
                setAccounts(allAccounts);
            })
        });
    }
    
    getAllAccounts();
    
    const bot = "BOT";
    
    function getUserName() {
        let user = accounts[accounts.length - 1];
        return user;
    }

    return (
        <Linkify>
            <div className="App">
                <GoogleButton />
                <div className="App-header">
                  <h1>Welcome to the Chatroom!</h1>
                </div>
                    <ol>
                        {
                            messages.map((message, index) => {
                                if (message.endsWith(".jpg") || message.endsWith(".png") || message.endsWith(".gif"))
                                    if(check(message) == 1)
                                        return  <li key={index}> <div className="botMessage"> <div className="botName"> {bot} </div> <div className="message"><p>{message}</p></div> </div></li>
                                    else
                                        return <li key={index}> <div className="messageSent"> <div className="userName"> {getUserName()}</div> <div className="message"><img src={message}></img></div></div></li>
                                else
                                    if(check(message) == 1)
                                        return  <li key={index}> <div className="botMessage"> <div className="botName"> {bot} </div> <div className="message"><p>{message}</p></div> </div></li>
                                    else
                                        return <li key={index}> <div className="messageSent"> <div className="userName"> {getUserName()}</div> <div className="message"><p> {message} </p></div></div></li>
                            })
                        }
                        
                    </ol>
                <Button />
            </div>
        </Linkify>
    );
}