import React from 'react';
import ReactDOM from 'react-dom/client';

import Layout from "../pages/layout/Layout";
import WindowOpeners from '../pages/WindowOpeners';
import { GlobalContext } from "../context";

const root = ReactDOM.createRoot(document.getElementById('root'));

// TODO: Pass a config from global val

root.render(
  <React.StrictMode>
    <GlobalContext.Provider value={window.dashboardData.context}>
        <Layout>
          <WindowOpeners windowOpeners={window.dashboardData.window_openers}/>
        </Layout>
      </GlobalContext.Provider>
  </React.StrictMode>
);

