import * as React from 'react';
import { observer } from 'mobx-react';
import UserStore from './UserStore';
import spotifyStore from './SpotifyStore';
import { withRouter, RouteComponentProps } from 'react-router-dom';

const TWO = 2;

interface Props {
    math: string;
}


@withRouter
class Account extends React.Component<any, any> {

    componentWillMount() {
        const token = this.props.match.params.token;
        console.log(token);
        UserStore.setToken(token);
        this.props.history.push('/');
    }

    render() {
        return(
            <div>Fallback</div>
        );
    }

}
export default Account;
