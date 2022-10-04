import React from "react";
import ReactDOM from "react-dom/client";

import Utils from "../pages/Utils";
import Layout from "../pages/layout/Layout";
import { GlobalContext } from "../context";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <GlobalContext.Provider value={window.dashboardData.context}>
      <Layout>
        <Utils />
      </Layout>
    </GlobalContext.Provider>
  </React.StrictMode>
);
