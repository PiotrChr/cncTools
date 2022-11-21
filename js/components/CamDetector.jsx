import React, { useState, useEffect, useRef, useCallback } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import PropTypes from 'prop-types'
import RoomMap from './RoomMap'
import CamView from './CamView'
import cls from 'classnames'
import SystemRepository from '../repository/systemRepository'
import { selectStingNotfications, notificationsStingAppend } from '../state/notifications'
import { selectStingCurrentHAngle } from '../state/stingControl'

const systemRepository = new SystemRepository()

const CamDetector = (props) => {
    const [status, setStatus] = useState('')
    const dispatch = useDispatch()
    const { detector } = props.camera
    const notifications = useSelector(selectStingNotfications())
    const currentHAngle = useSelector(selectStingCurrentHAngle()) || 0
    let timeoutId
    let intervalId = useRef(null)

    const startInterval = useCallback(() => {
        if (intervalId.current == null) {
            intervalId.current = setInterval(() => dispatch(notificationsStingAppend()), 1000)
        }
    }, [])

    const stopInterval = useCallback(() => {
        clearInterval(intervalId.current)
        intervalId.current = null;
    }, [])

    const startTracking = () => {
        systemRepository.startDetector()
        .then(() => {
            startInterval()
            refreshTrackerStatus()
        })
    }

    const stopTracking = () => {
        systemRepository.stopDetector()
        .then(() => {
            timeoutId = setTimeout(() => {
                stopInterval()
                refreshTrackerStatus()
            }, 500)
        })
    }

    const refreshTrackerStatus = () => {
        systemRepository.detectorStatus()
        .then(({data}) => {
            setStatus(data.full_status)
            if (data.status == 'active') {
                startInterval()
            } else {
                stopInterval()
            }
        })
    }

    useEffect(() => {
        refreshTrackerStatus()

        return () => {
            stopInterval()
        }
    }, [])

    const NotificationsC = React.memo((props) => {
        return (
            <div className="d-flex" id="detector_notifications" style={{ width:'60%' }}>
                { props.notifications.map((msg, index) => (
                    <div key={ index } className="detector_notification">
                        <div>
                            <span className="detector_notification_label">Date: </span><span>{ msg.date }</span>
                            <span className="detector_notification_label">Description: </span><span>{ msg.message.short }</span>
                        </div>
                        <div>
                            <div>
                                <span className="detector_notification_label">Confidence: </span>
                                <span>{ msg.message.full.confidence }</span>
                            </div>
                            <div>
                                <span className="detector_notification_label">Labels: </span>
                                <span>{ msg.message.full.labels.join(', ') }</span>
                            </div>
                            <div>
                                <span className="detector_notification_label">Detected label: </span>
                                <span>{ msg.message.full.detected_label }</span>
                            </div>
                        </div>

                    </div>

                )) }
            </div>
        )
    })

    return (
        <div className={ cls('col-12', props.className) }>
            <div className="card cam_card">
                <div className="card-body">
                    <div className="d-flex flex-column mt-3 mb-3">
                        <div className="d-flex align-items-stretch flex-lg-row flex-md-column flex-sm-column" id="detector_map_and_capture">
                            <div className="d-flex justify-content-center" id="detector_map" style={{ width: '100%'}}>
                                <RoomMap
                                    area={detector.room.area}
                                    shape={detector.room.shape}
                                    rov={detector.rov}
                                    currentHAngle={currentHAngle}
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
                            <NotificationsC notifications={ notifications } />
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

export default CamDetector