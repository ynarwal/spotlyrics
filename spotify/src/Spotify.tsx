import * as React from 'react';
import { withRouter, RouteComponentProps } from 'react-router';
import UserStore from './UserStore';
import RaisedButton from 'material-ui/RaisedButton';
import { observer } from 'mobx-react';
import spotifyStore from './SpotifyStore';
import CircularProgress from 'material-ui/CircularProgress';

@(withRouter as any)
@observer
export default class  Spotify extends  React.Component<any, any> {
    get injectedProps() {
        return this.props as RouteComponentProps<void>;
    }


    refresh = () => {
        spotifyStore.setCurrentSongLyrics();
    }

    render() {
        return(
            <div>
                <div className="error">{spotifyStore.error}</div>
                <RaisedButton
                    disabled={spotifyStore.loadingSong}
                    onClick={this.refresh}
                    label="Refresh"
                    primary={true}
                />
                <div className="">
                    {
                        spotifyStore.loadingSong && <CircularProgress />
                    }
                <br />
                <br />
                <div className="song" dangerouslySetInnerHTML={{ __html: spotifyStore.currentSongLyrics }} />

                </div>

            </div>
        );
    }

}
