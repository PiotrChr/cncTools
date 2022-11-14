import React from 'react'
import PropTypes from 'prop-types'
import RoomMap from './RoomMap'
import CamView from './CamView'

const CamDetector = (props) => {


    return (
        <div className="d-flex flex-column justify-content-between">
            <div className="d-flex" id="detector_map_and_capture">
                <div className="d-flex" id="detector_map">
                    <RoomMap />
                </div>
                <div className="d-flex" id="detector_capture">
                    <CamView
                        rotate={rotate}
                        source={ camera.source }
                        index={ index }
                        dynamic={ false }
                        id={ id }
                    />
                </div>
            </div>
            <div className="d-flex" id="detector_control_box">
            </div>
            <div className="d-flex" id="detector_notifications">
            </div>
        </div>
    )
}

CamDetector.propTypes = {
    fps: PropTypes.number
    rotate: PropTypes.number,
    detectorCaptureSource: PropTypes.string,
    id: PropTypes.number
}

CamDetector.defaultProps = {
    fps: 0,
    rotate: 0
}

export default CamDetector