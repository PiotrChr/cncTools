import React from 'react';
import ReactDOM from 'react-dom/client';

import Cameras from '../pages/Cameras';

const root = ReactDOM.createRoot(document.getElementById('root'));

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <Cameras />
  </React.StrictMode>
);

