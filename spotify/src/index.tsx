import * as React from 'react';
import * as ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Link,
  Switch,
} from 'react-router-dom';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import Account from './Account';
import './index.css';

function Routes() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={App} />
        <Route exact path="/account/:token" component={Account} />
        <Route path="*" component={() => <div>404 page not found</div>} />
      </Switch>
    </Router>
  );
}
const routes = Routes();
const mount = document.getElementById('root') as HTMLElement;


ReactDOM.render(routes, mount);
registerServiceWorker();
