import React from 'react'

export default (props) => {
    return (
        <div className="row mt-5">
            <div className="col-12">
                <div className="card cam_card">
                    <div className="card-body">
                        <h4 className="mt-2">Recording status</h4>
                        <p><span><strong>File name: </strong></span> { props.rec_status.recording_name }</p>
                        <p><span><strong>File path: </strong></span> { props.rec_status.name }</p>
                        <p><span><strong>Thread: </strong></span> { props.rec_status.thread_name }</p>
                        <p><span><strong>Started at: </strong></span> { props.rec_status.started }</p>
                        <p><span><strong>Width: </strong></span> { props.rec_status.width }</p>
                        <p><span><strong>Height: </strong></span> { props.rec_status.height }</p>
                        <p><span><strong>Fps: </strong></span> { props.rec_status.fps }</p>
                    </div>
                </div>
            </div>
        </div>
    )
}