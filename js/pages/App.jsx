import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { createBrowserHistory } from "history";

import Layout from './pages/layout/Layout'

const loading = (
    <div className="pt-3 text-center">
        <div className="sk-spinner sk-spinner-pulse"></div>
    </div>
)

// Containers
const Home = React.lazy(() => import('./pages/Home'));
const Cameras = React.lazy(() => import('./pages/Cameras'));
const SingleCamera = React.lazy(() => import('./pages/SingleCamera'));
const Relays = React.lazy(() => import('./pages/Relays'));
const WindowOpeners = React.lazy(() => import('./pages/WindowOpeners'));

// Pages
const Page404 = React.lazy(() => import('./pages/page404/Page404'));
const Page500 = React.lazy(() => import('./pages/page500/Page500'));

// const basename = window.bayramo_status.basename // TODO: Get basename
const basename = '/sec'

class App extends Component {

    render() {
        return (
            <Router history={createBrowserHistory()}>
                <React.Suspense fallback={loading}>
                    <Layout>
                        <Routes>
                            <Route exact path="/500" name="Page 500" element={<Page500/>} />
                            <Route exact path={basename} name="Home" element={<Home/>} />
                            <Route path={basename + '/cameras'} name="Returns Add" element={<Cameras/>} />
                            <Route path={basename + '/single'} name="Returns View" element={<SingleCamera/>} />
                            <Route path={basename + '/relays'} name="Returns View" element={<Relays/>} />
                            <Route path={basename + '/window_openers'} name="Returns View" element={<WindowOpeners/>} />
                            <Route name="Page 404" element={<Page404/>} />
                        </Routes>
                    </Layout>
                </React.Suspense>
            </Router>
        );
    }
}

export default App;