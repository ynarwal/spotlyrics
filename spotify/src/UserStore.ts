import { autorun, observable } from 'mobx';
import * as request from 'request';
const TOKEN_STR = 'token';
const CODE_STR = 'code';
const DATE_STR = 'exp';

class UserStore {
    @observable spotifyToken = '';
    @observable expiryDate: Date;
    @observable code: string = '';
    @observable logging = false;

    setToken(token: string) {
        localStorage.setItem(TOKEN_STR, token);
        this.spotifyToken = token;
    }

    logout() {
        localStorage.removeItem(TOKEN_STR);
        this.spotifyToken = '';
    }

    isUserLoggedIn() {
        return this.spotifyToken !== '';
    }

    hasTokenExpired() {
        if (this.spotifyToken === '') {
            return true;
        }
        const dateStr = localStorage.getItem(DATE_STR);
        if (dateStr !== null) {
            const expiryDate = new Date(dateStr);
            const now = new Date();
            return now > expiryDate;
        }
        return true;
    }

    setExpiryDate(seconds: number) {
        console.log(seconds);
        const t = new Date();
        t.setSeconds(t.getSeconds() + seconds);
        this.expiryDate = t;
        localStorage.setItem(DATE_STR, t.toString());
    }


    getCookie(cname: string) {
        const name = cname + '=';
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) === 0) {
                return c.substring(name.length, c.length);
            }
        }
        return '';
    }
}


const userStore = new UserStore();
autorun(() => {
    const token = localStorage.getItem(TOKEN_STR);
    const code = localStorage.getItem(CODE_STR);
    if (token !== null) {
        userStore.setToken(token);
    }
});

export default userStore;
