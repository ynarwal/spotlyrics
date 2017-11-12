import * as React from 'react';
import './App.css';
import UserStore from './UserStore';
import { observer } from 'mobx-react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import RaisedButton from 'material-ui/RaisedButton';
import Spotify from './Spotify';
const logo = require('./logo.svg');

interface State {
  todoValue: String;
}

@observer
class App extends React.Component<{}, State> {

  constructor() {
    super();
    this.state = {
      todoValue: '',
    };
  }


  login = () => {
    const url = `${process.env.REACT_APP_URL}/accounts/spotify/login/?process=login`;
    window.location.replace(url);
  }

  logout = () => {
     UserStore.logout();
  }

  ontodoValueChange = (event: any) => {
    this.setState({
      todoValue: event.currentTarget.value,
    },            () => {
      console.log(this.state.todoValue);
    });
  }

  onSpotifyClick = () => {
    //
  }

  render() {
    return (
      <MuiThemeProvider >
        <div className="App">
            <h2>Welcome to Current-lyrics</h2>
            <div hidden={UserStore.isUserLoggedIn()}>
                <RaisedButton onClick={this.login} label="Login" primary={false} />
            </div>
            <div hidden={!UserStore.isUserLoggedIn()}>
                <Spotify />
            </div>
        </div>
      </MuiThemeProvider>
    );
  }
}

export default App;
