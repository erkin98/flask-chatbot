import './App.css';
import {useCallback, useEffect} from 'react';
import axios from 'axios';
import  {BrowserRouter as Router,Route,Switch} from 'react-router-dom';
import Chat from "./Chat";
// import Login from "./Login";
import Sidebar from "./Sidebar";
import { useStateValue } from './StateProvider';


function App() {
  const [state,dispatch] = useStateValue();
  
  const fetchData = useCallback(async() => {
    try{
      const res = await axios.get('/customers');
      dispatch({ type: "GET_CUSTOMERS", customers: res.data.data });
      return res;
    }catch(err){ console.log(err) }
  },[dispatch])

  useEffect(() => {
      fetchData();
  }, [fetchData]);

  return (
    <div className="app">
      <div className="app__body">
          <Router>
            <Sidebar refreshHandler={fetchData}/>
            <Switch>
              <Route path="/rooms/:roomId">
                <Chat />
              </Route>
              <Route path="/"></Route>
            </Switch>
          </Router>
        </div>
    </div>
  );
}

export default App;
