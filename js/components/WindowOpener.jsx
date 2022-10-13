import React, { useState } from 'react'

const WindowOpener = (props) => {

    return (
      <div className="row mb-3 mt-3">
        <div className="col-12">
          <div className="card cam_card">
            <div className="card-body">
              <h5 className="card-title cnc_card-title">{props.opener.name}</h5>
              <div className="d-flex align-items-center justify-content-between">
                <div
                  className="d-flex align-items-center justify-content-between"
                  style={{ minWidth: "150px" }}
                >
                  <a
                    onClick={props.onOpen}
                    className="btn btn-success cnc_card-button mr-3"
                  >
                    Open
                  </a>
                  <a
                    onClick={props.onClose}
                    className="btn btn-danger cnc_card-button"
                  >
                    Close
                  </a>
                </div>

                <div
                  className="d-block"
                  style={{ width: "100%", margin: "0 20px" }}
                >
                  <div className="form-group">
                    <input
                      type="range"
                      name="open_to_value"
                      min="0"
                      max="100"
                      step="5"
                      className="form-range"
                    />
                  </div>
                </div>
                <button type="submit" className="btn btn-primary me-1">
                  Set
                </button>
              </div>

              <div className="d-flex flex-row justify-content-center">
                Currently opened to: <strong>somealue</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
}

export default WindowOpener