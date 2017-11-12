import { autorun, observable } from 'mobx';
import userStore from './UserStore';
import * as request from 'request';
const TOKEN_STR = 'token';
const DATE_STR = 'exp';
const NOT_PLAYING_STATUS = 204;
const CURRENTLY_PLAYING_API = `${process.env.REACT_APP_URL}/api/get-current-song-lyrics/`;
class SpotifyStore {
    @observable playing = false;
    @observable currentSongLyrics: '';
    @observable error = '';
    @observable loadingSong = false;

    callback = (error: any, response: any, body: any) => {
        const lyrics = JSON.parse(body).lyrics;
        if (lyrics !== undefined) {
            this.currentSongLyrics = lyrics.replace(/\n/g, '<br />');
        }
        this.loadingSong = false;
    }

    setCurrentSongLyrics () {
        if (userStore.isUserLoggedIn()) {
            this.loadingSong = true;
            const token = 'Token ' + userStore.spotifyToken;
            const options = {
                url: CURRENTLY_PLAYING_API,
                headers: {
                    Authorization: token,
                },
            };
            request.get(options, this.callback);
        }
    }
}

const spotifyStore = new SpotifyStore();
export default spotifyStore;
