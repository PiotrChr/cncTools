import React, { useContext, useState, useEffect } from 'react'
import { GlobalContext } from '../context'
import Recordings from '../components/Recordings'
import RecStatus from '../components/RecStatus'
import CamControls from '../components/CamControls'
import CamView from '../components/CamView'
import RecordingsRepository from '../repository/recordingsRepository'
import { useCallback } from 'react'

const recordingsRepository = new RecordingsRepository()

export default (props) => {
    const [recordings, setRecordings] = useState(null)
    const [recStatus, setRecStatus] = useState(null)
    const context = useContext(GlobalContext)
    
    const { camera } = props
    const rotate = camera.rotate ?? 0

    let intervalId;

    useEffect(() => {
        fetchStatus()

        if (recStatus) {
            intervalId = setInterval(fetchStatus, 2000)
        }

        return () => {
            clearInterval(intervalId)
        }
    }, [])

    const fetchStatus = () => {
        recordingsRepository.getRecStatusForCam(camera.id).then((data) => {
          setRecordings(data.recordings);
          setRecStatus(data.status);
        });
    }

    const startRecord = useCallback(() => {
        recordingsRepository.startRecording(camera.id)
        setTimeout(fetchStatus, 1000)
    }, [])

    const stopRecord = useCallback(() => {
        recordingsRepository.stopRecording(camera.id);
        setTimeout(fetchStatus, 500);
    })

    return (
        <div className='row'>
            <div className='col-12'>
                <div className='card cam_card'>
                    <CamView source={ camera.source } rotate={ rotate } index={ camera.id } dynamic={ camera.type == 'dynamic' } id={ camera.id }/>
                    <div className="card-body">
                        <h5 className="card-title cnc_card-title">{ camera.name }</h5>
                        <div className="d-flex  flex-column justify-content-between mt-5" style={{ clear: "both" }}>
                            <div>
                                <a href="/sec" className="btn btn-primary cnc_card-button">Back</a>
                                { recStatus
                                    ? <a onClick={ stopRecord } className="btn btn-danger cnc_card-button">Stop Recording</a>
                                    : <a onClick={ startRecord } className="btn btn-success cnc_card-button me-5">Start Recording</a>
                                }
                            </div>
                            
                            { camera.move && <CamControls camera={camera}/> }
                        </div>
                    </div>
                </div>
            </div>
            { recStatus && <RecStatus { ...recStatus }/> }
            { recordings && <Recordings recordings={recordings}/> }
        </div>
    )
}