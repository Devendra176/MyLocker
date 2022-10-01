import React from 'react';
import NavBarComponent from './Components/navbar';
import {NavPath} from './Router/NavRoutes';

function App() {
  return (
      <div className="App">
        <NavBarComponent />
        <NavPath />
      </div>
  );
}

export default App;
