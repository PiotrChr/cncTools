import React, { useContext, useCallback } from 'react'
import SystemRepository from "../repository/systemRepository";

const systemRepository = new SystemRepository();


const Utils = (props) => {

    const rebootSting = useCallback(() => {
        systemRepository.rebootSting()
        .then((data) => {
            alert(data.status)
        })
    }, [])

    return (
      <div className="row">
        <div className='d-flex'>
          <a
            id="camera_control_down"
            onClick={ rebootSting }
            className="btn btn-danger d-block mt-4"
          >
            Reboot Sting
          </a>
        </div>
      </div>
    );
}

export default Utils