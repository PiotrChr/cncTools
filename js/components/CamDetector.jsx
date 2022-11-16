import React, { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import RoomMap from './RoomMap'
import CamView from './CamView'
import cls from 'classnames'
import SystemRepository from '../repository/systemRepository'

const systemRepository = new SystemRepository()

const CamDetector = (props) => {
    const [status, setStatus] = useState('')

    const { detector } = props.camera
    let timeoutId = null

    const startTracking = () => {
        systemRepository.startDetector()
        .then(() => {
            setTimeout(refreshTrackerStatus, 500)
        })
    }

    const stopTracking = () => {
        systemRepository.stopDetector()
        .then(() => {
            setTimeout(refreshTrackerStatus, 500)
        })
    }

    const refreshTrackerStatus = () => {
        systemRepository.detectorStatus()
        .then(({data}) => {
            setStatus(data.full_status)
        })
    }

    useEffect(() => {
        refreshTrackerStatus()
    }, [])

    return (
        <div className={ cls('col-12', props.className) }>
            <div className="card cam_card">
                <div className="card-body">
                    <div className="d-flex flex-column mt-3 mb-3">
                        <div className="d-flex align-items-stretch flex-row" id="detector_map_and_capture">
                            <div className="d-flex justify-content-center" id="detector_map" style={{ width: '100%'}}>
                                <RoomMap
                                    area={detector.room.area}
                                    shape={detector.room.shape}
                                    rov={detector.rov}
                                    currentHAngle={props.currentHAngle}
                                    hRange={detector.range.h}
                                    cameraPosition={detector.cam_position.loc}
                                    defPosAngle={detector.cam_position.def_pos_angle}
                                />
                            </div>
                            <div className="d-flex" id="detector_capture" style={{ width: '100%'}}>
                                <CamView
                                    rotate={ detector.cam.rotate }
                                    source={ detector.cam.source }
                                    index={ detector.cam.id }
                                    dynamic={ false }
                                    id={ detector.cam.id }
                                    style={{ marginLeft: '10px', height: detector.room.area[1]+"px" }}
                                />
                            </div>
                        </div>
                        <div className="d-flex mt-5 mb-5 justify-content-around" id="detector_control_box">
                            <a id="detector_refresh_tracker_status"
                               onClick={ refreshTrackerStatus }
                               className="btn btn-danger"
                            >Detector status</a>
                            <a id="detector_start_tracking"
                               onClick={ startTracking }
                               className="btn btn-success"
                            >Start detector</a>
                            <a id="detector_stop_tracking"
                               onClick={ stopTracking }
                               className="btn btn-danger"
                            >Stop detector</a>
                        </div>
                        <div className="d-flex" id="detector_notifications_and_status">
                            <div className="d-flex" id="detector_status" style={{ width:'40%' }}>
                                <pre style={{ fontSize: '0.5rem', overflow: 'hidden' }}>
                                    { status }
                                </pre>

                            </div>
                            <div className="d-flex" id="detector_notifications" style={{ width:'60%' }}></div>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

CamDetector.propTypes = {
    camera: PropTypes.object,
    currentHAngle: PropTypes.number
}

CamDetector.defaultProps = {

}

export default CamDetector