import React from 'react'
import PropTypes from 'prop-types'

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
                        <a onClick={ () => props.onPlay(props.cameraId, recording.file) } className="btn btn-success cnc_card-button">
                          Play
                        </a>
                      </td>
                      <td>
                        <a onClick={ () => props.onRemove(props.cameraId, recording.file) } className="btn btn-danger cnc_card-button">
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
    recordings: [],
}

Recordings.propTypes = {
  recordings: PropTypes.array,
  onRemove: PropTypes.func,
  onPlay: PropTypes.func,
  cameraId: PropTypes.number
}

export default Recordings