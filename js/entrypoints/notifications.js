import React from 'react';
import ReactDOM from 'react-dom/client';

import Layout from '../pages/layout/Layout'
import Notifications from '../pages/Notifications';
import { GlobalContext } from '../context'

const root = ReactDOM.createRoot(document.getElementById('root'));

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <GlobalContext.Provider value={window.dashboardData.context}>
      <Layout>
        <Notifications />
      </Layout>
    </GlobalContext.Provider>    
  </React.StrictMode>
);

