import React from 'react'

export default (props) => {
    return (
        <div className="col-12">
            <div className="card cam_card">
                <div className="card-body">
                    <h4 className="mt-2">Recording status</h4>
                    <p><span><strong>File name: </strong></span> { props.recording_name }</p>
                    <p><span><strong>File path: </strong></span> { props.name }</p>
                    <p><span><strong>Thread: </strong></span> { props.thread_name }</p>
                    <p><span><strong>Started at: </strong></span> { props.started }</p>
                    <p><span><strong>Width: </strong></span> { props.width }</p>
                    <p><span><strong>Height: </strong></span> { props.height }</p>
                    <p><span><strong>Fps: </strong></span> { props.fps }</p>
                </div>
            </div>
        </div>
    )
}