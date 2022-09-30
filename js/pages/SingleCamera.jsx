import React, { useContext } from 'react'
import { GlobalContext } from '../context'
import Recordings from '../components/Recordings'
import RecStatus from '../components/RecStatus'
import CamControls from '../components/CamControls'
import CamView from '../components/CamView'

export default (props) => {
    const context = useContext(GlobalContext)
    const { camera } = props
    const rotate = camera.rotate ?? 0

    const rec_status = false
    const recordings = false

    return (
        <div className='row'>
            <div className='col-12'>
                <div className='card cam_card'>
                    <CamView source={ camera.source } rotate={ rotate } index={ camera.id } dynamic={ camera.type == 'dynamic' }/>
                    <div className="card-body">
                        <h5 className="card-title cnc_card-title">{ camera.name }</h5>
                        <div className="d-flex  flex-column justify-content-between mt-5" style={{ clear: "both" }}>
                            <div>
                                <a href="/sec" className="btn btn-primary cnc_card-button">Back</a>
                                { rec_status
                                    ? <a href="urlforstoprecord" className="btn btn-danger cnc_card-button">Stop Recording</a>
                                    : <a href="urlforstartrecord" className="btn btn-success cnc_card-button">Start Recording</a>
                                }
                            </div>
                            
                            { camera.move && <CamControls camera={camera}/> }
                        </div>
                    </div>
                </div>
            </div>
            { rec_status && <RecStatus /> }
            { recordings && <Recordings /> }
        </div>
    )
}