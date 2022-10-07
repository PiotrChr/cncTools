import React from 'react';
import ReactDOM from 'react-dom/client';

import WindowOpeners from '../pages/WindowOpeners';

const root = ReactDOM.createRoot(document.getElementById('root'));

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <WindowOpeners />
  </React.StrictMode>
);

