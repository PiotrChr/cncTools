import React from 'react'
import PropTypes from 'prop-types'
import { NavLink } from 'react-router-dom'

import {
  CHeader,
  CToggler,
  CHeaderBrand,
  CHeaderNav,
  CNavItem,
  CNavLink,
  CSubheader,
  CBreadcrumbRouter,
  CLink
} from '@coreui/react'
import CIcon from '@coreui/icons-react'

// TODO: Get links from conf/ maybe context

const Header = (props) => {
  return (
    <CHeader>
      <CHeaderNav className="d-none d-md-flex me-auto">
        <CNavItem className="px-3" >
          <CNavLink to="/" component={NavLink}>Home</CNavLink>
        </CNavItem>
        <CNavItem className="px-3" >
          <CNavLink to="/bookings" component={NavLink}>Bookings</CNavLink>
        </CNavItem>
        <CNavItem className="px-3" >
            <CNavLink to="/cars" component={NavLink}>Cars</CNavLink>
        </CNavItem>
        <CNavItem className="px-3" >
            <CNavLink to="/offices" component={NavLink}>Offices</CNavLink>
        </CNavItem>
      </CHeaderNav>
    </CHeader>
  )
}

Header.propTypes = {
    user: PropTypes.object
}

Header.defaultProps = {
    user: {
        username: 'Username'
    }
}

export default Header