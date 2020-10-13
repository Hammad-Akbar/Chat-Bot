import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';
import './Content.css';

function randomName() {
  const adjectives = [
    "autumn", "hidden", "bitter", "misty", "silent", "empty", "dry", "dark",
    "summer", "icy", "delicate", "quiet", "white", "cool", "spring", "winter",
    "patient", "twilight", "dawn", "crimson", "wispy", "weathered", "blue",
    "billowing", "broken", "cold", "damp", "falling", "frosty", "green", "long",
    "late", "lingering", "bold", "little", "morning", "muddy", "old", "red",
    "rough", "still", "small", "sparkling", "throbbing", "shy", "wandering",
    "withered", "wild", "black", "young", "holy", "solitary", "fragrant",
    "aged", "snowy", "proud", "floral", "restless", "divine", "polished",
    "ancient", "purple", "lively", "nameless"
  ];
  
  const nouns = [
    "waterfall", "river", "breeze", "moon", "rain", "wind", "sea", "morning",
    "snow", "lake", "sunset", "pine", "shadow", "leaf", "dawn", "glitter",
    "forest", "hill", "cloud", "meadow", "sun", "glade", "bird", "brook",
    "butterfly", "bush", "dew", "dust", "field", "fire", "flower", "firefly",
    "feather", "grass", "haze", "mountain", "night", "pond", "darkness",
    "snowflake", "silence", "sound", "sky", "shape", "surf", "thunder",
    "violet", "water", "wildflower", "wave", "water", "resonance", "sun",
    "wood", "dream", "cherry", "tree", "fog", "frost", "voice", "paper", "frog",
    "smoke", "star"
  ];
  const adjective = adjectives[Math.floor(Math.random() * adjectives.length)];
  const noun = nouns[Math.floor(Math.random() * nouns.length)];
  const user = adjective + "_" + noun;
  return user;
}

function check(message) {
    if (message.startsWith(" ")) {
        return message;
    }
    else {
        message = " ";
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
        message = " ";
        return message;
    }
}

export function Content() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessages() {
        
        React.useEffect(() => {
            Socket.on('messages received', (data) => {
                console.log("Received messages from server: " + data['allmessages']);
                setMessages(data['allmessages']);
            })
        });
    }
    
    getNewMessages();
    
    const name = "icy_wind (BOT)";
    
    let user = randomName();

    
    return (
        <div className="App">
            <div className="App-header">
              <h1>Welcome to the Chatroom!</h1>
            </div>
                <ol>
                    {
                        messages.map((message, index) =>
                            <li key={index}> 
                                <div className="messageSent"> <div className="userName"> {user.toUpperCase()}</div> <div className="message"><p> {checkNot(message)} </p></div></div>
                                <div className="botMessage"> <div className="botName"> {name.toUpperCase()}: </div> <div className="message"><p>{check(message)}</p></div> </div>
                            </li>
                        )
                    }
                    
                </ol>
            <Button />
        </div>
    );
}