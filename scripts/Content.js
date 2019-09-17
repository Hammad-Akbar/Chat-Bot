    
import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': []
        };
    }
    
    componentDidMount() {
        Socket.on('number received', (data) => {
            this.setState({
                'number_received': data['number']
            });
        })
    }

    render() {
        let my_rand_num = this.state.number_received
        return (
            <div>
                <h1>Random number!</h1>
                <ul>{my_rand_num}</ul>
                <Button />
            </div>
        );
    }
}