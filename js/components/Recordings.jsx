import React from 'react'

export default (props) => {

    return (
        <div className="row mt-5">
            <div className="col-12">
                <div className="card cam_card">
                    <div className="card-body">
                        <h4>Recordings</h4>

                        <table className="table">
                            <tr>
                                <th></th>
                                <th></th>
                                <th></th>
                            </tr>
                            {
                                props.recordings.map((recording, index) => (
                                    <tr key={ index }>
                                        <td>{ recording.file }</td>
                                        <td>
                                            <a href="urlforsinglevid" className="btn btn-success cnc_card-button">
                                                Play
                                            </a>
                                        </td>
                                        <td>
                                            <a href="urlfordeleterecord" clasName="btn btn-danger cnc_card-button">
                                                Remove
                                            </a>
                                        </td>
                                    </tr>
                                ))
                            }
                        </table>
                    </div>
                </div>
            </div>
        </div>
    )
}