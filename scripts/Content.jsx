import * as React from 'react';
import Linkify from 'react-linkify';
import Button from './Button';
import Socket from './Socket';
import GoogleButton from './GoogleButton';
import './Content.css';

function check(message) {
  if (message.startsWith(' ')) {
    return 1;
  }

  return 0;
}

export default function Content() {
  const [messages, setMessages] = React.useState([]);
  const [accounts, setAccounts] = React.useState([]);

  function getNewMessages() {
    React.useEffect(() => {
      Socket.on('messages received', (data) => {
        setMessages(data.allmessages);
      });
    });
  }

  getNewMessages();

  function getAllAccounts() {
    React.useEffect(() => {
      Socket.on('users updated', (data) => {
        const allAccounts = data.allUsers;
        setAccounts(allAccounts);
      });
    });
  }

  getAllAccounts();

  const bot = 'BOT';

  function getUserName() {
    const user = accounts[accounts.length - 1];
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
                              if (message.endsWith('.jpg') || message.endsWith('.png') || message.endsWith('.gif')) {
                                if (check(message) === 1) {
                                  return (
                                    <li key={index}>
                                      {' '}
                                      <div className="botMessage">
                                        {' '}
                                        <div className="botName">
                                          {' '}
                                          {bot}
                                          {' '}
                                        </div>
                                        {' '}
                                        <div className="message"><p>{message}</p></div>
                                        {' '}
                                      </div>
                                    </li>
                                  );
                                }
                                return (
                                  <li key={index}>
                                    {' '}
                                    <div className="messageSent">
                                      {' '}
                                      <div className="userName">
                                        {' '}
                                        {getUserName()}
                                      </div>
                                      {' '}
                                      <div className="message"><img src={message} alt="pic" /></div>
                                    </div>
                                  </li>
                                );
                              }
                              if (check(message) === 1) {
                                return (
                                  <li key={index}>
                                    {' '}
                                    <div className="botMessage">
                                      {' '}
                                      <div className="botName">
                                        {' '}
                                        {bot}
                                        {' '}
                                      </div>
                                      {' '}
                                      <div className="message"><p>{message}</p></div>
                                      {' '}
                                    </div>
                                  </li>
                                );
                              }
                              return (
                                <li key={index}>
                                  {' '}
                                  <div className="messageSent">
                                    {' '}
                                    <div className="userName">
                                      {' '}
                                      {getUserName()}
                                    </div>
                                    {' '}
                                    <div className="message">
                                      <p>
                                        {' '}
                                        {message}
                                        {' '}
                                      </p>
                                    </div>
                                  </div>
                                </li>
                              );
                            })
                        }

        </ol>
        <Button />
      </div>
    </Linkify>
  );
}
