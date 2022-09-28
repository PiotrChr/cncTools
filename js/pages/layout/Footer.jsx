import React from 'react'
import { CFooter } from '@coreui/react'

// TODO: Add a proper name

const Footer = () => {
  return (
    <CFooter fixed="false">
      <div>
        <span className="ml-1">Dashboard</span>
      </div>
      <div className="mfs-auto">
        <span className="mr-1">Powered by</span>
        <a href="https://coreui.io/react" target="_blank" rel="noopener noreferrer">CoreUI for React</a>
      </div>
    </CFooter>
  )
}

export default React.memo(Footer)