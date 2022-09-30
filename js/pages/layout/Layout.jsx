import React from 'react'
import PropTypes from 'prop-types';
import Footer from './Footer'
import Header from './Header'

const Layout = (props) => (
    <div className="c-app c-default-layout">
      <div className="c-wrapper">
        <Header />
        <div className="container-fluid">
            { props.children }
        </div>
      <Footer />
      </div>
    </div>
  )


Layout.propTypes = {
    children: PropTypes.any
}

export default Layout