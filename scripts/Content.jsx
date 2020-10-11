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
  const name = adjective + "_" + noun + " (BOT)";
  return name;
}

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

    const name = "autumn_wind (BOT)";
    
    return (
        <div className="App">
            <div className="App-header">
              <h1>Welcome to the Chatroom!</h1>
            </div>
                <ol>
                    {
                        messagees.map(
                            (message, index) =>
                                <li key={index}> <div className="botName"> {name.toUpperCase()}: </div> <div className="message"><p>{message}</p></div> </li>
                        )
                    }
                </ol>
            <Button />
        </div>
    );
}
