import React from 'react'

// TODO: Add a proper name

const Footer = () => {
  return (
    <footer className="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <div className="col-md-4 d-flex align-items-center">
          <span className="mb-3 mb-md-0 text-muted">© 2022 Piotr C Smartflat Dashboard</span>
        </div>
    </footer>
  )
}

export default React.memo(Footer)