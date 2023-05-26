import React, { useContext } from 'react'
import PropTypes from 'prop-types'
import { GlobalContext } from '../../context'
import classnames from 'classnames'

// TODO: Get links from conf/ maybe context

const Header = (props) => {
  const context = useContext(GlobalContext)
  
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className='collapse navbar-collapse'>
            <ul className="navbar-nav mr-auto">
                { context.menu.map((item, index) => (
                    <li className="nav-item" key="1" key={index}>
                        <a className={ classnames("nav-link", item.route==context.current_url ? "active" : "") } href={ item.route }>
                            { item.name }
                        </a>
                    </li>
                )) }
            </ul>
        </div>
        
    </nav>
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