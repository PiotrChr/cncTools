import React from 'react'


export default (props) => {
    const camera = props.camera

    const refresh = useCallback(() => {
        first
      },
      [],
    )
    

    return (
      <div>
        <div className="d-flex align-items-center flex-row">
          <div className="camera_control d-flex align-items-center">
            <div>
              <a
                id="camera_control_left"
                href={camera.api + camera.move.step.h + "-1"}
                className="btn d-block"
              >
                <i className="fa fa-arrow-left" />
              </a>
            </div>
            <div>
              <a
                id="camera_control_up"
                href={camera.api + camera.move.step.v + "-1"}
                className="btn clearfix d-block mb-4"
              >
                <i className="fa fa-arrow-up" />
              </a>
              <a
                id="camera_control_down"
                href={camera.api + camera.move.step.v + "1"}
                className="btn d-block mt-4"
              >
                <i className="fa fa-arrow-down" />
              </a>
            </div>
            <div>
              <a
                id="camera_control_right"
                href={camera.api + camera.move.step.h + "1"}
                className="btn d-block"
              >
                <i className="fa fa-arrow-right" />
              </a>
            </div>
          </div>

          <div
            className="d-block"
            style={{ width: "100%", marginLeft: "10px" }}
          >
            <div className="form-group">
              <label htmlFor="vRange" className="form-label">
                Vertical destination
              </label>
              <input type="range" className="form-range" id="vRange_dest" />
            </div>
            <div className="form-group">
              <label htmlFor="vRange" className="form-label">
                Vertical position
              </label>
              <input type="range" className="form-range" id="vRange_pos" disabled/>
            </div>

            <div className="form-group">
              <label htmlFor="hRange" className="form-label">
                Horizontal destination
              </label>
              <input type="range" className="form-range" id="hRange_dest" />
            </div>
            <div className="form-group">
              <label htmlFor="hRange" className="form-label">
                Horizontal position
              </label>
              <input type="range" className="form-range" id="hRange_pos" disabled/>
            </div>
          </div>
        </div>

        <div
          className="d-flex flex-md-row flex-sm-column flex-xs-column justify-content-between mt-5"
          style={{ clear: "both" }}
        >
          <a
            id="camera_control_reset"
            href="#"
            className="btn btn-primary cnc_card-button mt-2"
          >
            Reset
          </a>
          <a
            id="camera_control_stop"
            href="#"
            className="btn btn-danger cnc_card-button mt-2"
          >
            Stop
          </a>
          <a
            id="camera_control_idle"
            href="#"
            className="btn btn-success cnc_card-button mt-2"
          >
            Idle
          </a>
          <a
            id="camera_control_auto_idle_on"
            href="#"
            className="btn btn-success cnc_card-button mt-2"
          >
            Auto-Idle On
          </a>
          <a
            id="camera_control_auto_idle_off"
            href="#"
            className="btn btn-danger cnc_card-button mt-2"
          >
            Auto-Idle Off
          </a>
          <a
            id="camera_control_idle_v_off"
            href="#"
            className="btn btn-danger cnc_card-button mt-2"
          >
            Idle V Off
          </a>
          <a
            id="camera_control_idle_v_on"
            href="#"
            className="btn btn-success cnc_card-button mt-2"
          >
            Idle V On
          </a>
          <a
            id="camera_control_idle_h_off"
            href="#"
            className="btn btn-danger cnc_card-button mt-2"
          >
            Idle H Off
          </a>
          <a
            id="camera_control_idle_h_on"
            href="#"
            className="btn btn-success cnc_card-button mt-2"
          >
            Idle H On
          </a>
        </div>
      </div>
    );
}