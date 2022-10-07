import React from 'react'

const Recordings = (props) => {
    if (!props.recordings || props.recordings.length == 0) return null

    return (
      <div className="row mt-5">
        <div className="col-12">
          <div className="card cam_card">
            <div className="card-body">
              <h5>Recordings</h5>

              <table className="table">
                <thead>
                  <tr>
                    <th></th>
                    <th></th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  {props.recordings.map((recording, index) => (
                    <tr key={index}>
                      <td>{recording.file}</td>
                      <td>
                        <a href="urlforsinglevid" className="btn btn-success cnc_card-button">
                          Play
                        </a>
                      </td>
                      <td>
                        <a href="urlfordeleterecord" className="btn btn-danger cnc_card-button" >
                          Remove
                        </a>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    );
}

Recordings.defaultProps = {
    recordings: []
}

export default Recordings