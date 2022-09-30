import React, { useContext } from 'react'
import { GlobalContext } from '../context'
import CamView from '../components/CamView'

export default (props) => {
    const context = useContext(GlobalContext)

    if (typeof props.cameras == 'undefined' || props.cameras.length == 0) {
        return 'No cameras'
    }

    const renderCameras = () => {
        return props.cameras.map((camera, index) => {
            const rotate = (typeof camera.rotate !== 'undefined') ? camera.rotate : 0;
            
            return (
                <div className="col-xl-3 col-lg-4 col-md-6 col-sm-12 label" key={ index }>
                    <div className="card cam_card">
                        <CamView rotate={rotate} source={ camera.source } index={ index } dynamic={ camera.type == "dynamic" }/>
                        { camera.move &&
                            <div style={{position: 'absolute', right: '20px', color: 'white', fontSize: '40px'}}>
                                <i className="fa fa-gamepad"></i>
                            </div>
                        }
                        <div className="card-body d-flex flex-column">
                            <div>
                                <h5 className="card-title cnc_card-title">{ camera.name }</h5>
                            </div>
                            <div className="d-flex flex-row justify-content-between align-items-center">
                                <a href={ context.routes.main.single_cam + "?r=" + camera.id } className="btn btn-primary cnc_card-button">Inspect</a>
                            </div>
                        </div>
                    </div>
                </div>
            )
            
        })
    }

    return (
        <div className="row">
            { renderCameras() }
        </div>
    )
}