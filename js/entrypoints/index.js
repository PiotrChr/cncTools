import React from 'react';
import ReactDOM from 'react-dom/client';

import App from '../pages/Home';

const root = ReactDOM.createRoot(document.getElementById('root'));

console.log("Here")

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <Home />
  </React.StrictMode>
);

