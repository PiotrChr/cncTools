import React from 'react';
import ReactDOM from 'react-dom/client';

import Relays from '../pages/Relays';

const root = ReactDOM.createRoot(document.getElementById('root'));

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <Relays />
  </React.StrictMode>
);

