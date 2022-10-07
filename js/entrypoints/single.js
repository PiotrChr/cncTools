import React from 'react';
import ReactDOM from 'react-dom/client';

import SingleCamera from '../pages/SingleCamera';
import Layout from '../pages/layout/Layout';
import { GlobalContext } from '../context'

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
      <GlobalContext.Provider value={window.dashboardData.context}>
        <Layout>
          <SingleCamera camera={ window.dashboardData.camera }/>
        </Layout>        
    </GlobalContext.Provider>
  </React.StrictMode>
);

