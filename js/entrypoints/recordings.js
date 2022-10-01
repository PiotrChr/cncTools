import React from "react";
import ReactDOM from "react-dom/client";

import Layout from "../pages/layout/Layout";
import Recordings from "../pages/Recordings";
import { GlobalContext } from "../context";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <GlobalContext.Provider value={window.dashboardData.context}>
      <Layout>
        <Recordings cameras={window.dashboardData.cameras} />
      </Layout>
    </GlobalContext.Provider>
  </React.StrictMode>
);
