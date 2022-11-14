import React, { useState, useEffect, useCallback } from 'react'
import classnames from 'classnames'
import StingControlRepository from '../repository/stingControlRepository'

const stingControlRepository = new StingControlRepository()

const DEFAULT_POS = { v: 0, h: 0 }
const TRACK_RATE = 1000

const V_MAX = 115
const V_MIN = 75
const V_STEP = (V_MAX - V_MIN) / 10

const H_MAX = 180
const H_MIN = 0
const H_STEP = (H_MAX - H_MIN) / 30;

const MOTORS = {'h': 0, 'v': 1}

export default (props) => {
    const camera = props.camera
    const [currentPos, setCurrentPos] = useState(DEFAULT_POS)
    const [targetPos, setTargetPos] = useState(DEFAULT_POS);
    const [autoIdle, setAutoIdle] = useState(false)
    const [idle, setIdle] = useState(false)
    const [idleMoveRight, setIdleMoveRight] = useState(true)
    const [idleMoveUp, setIdleMoveUp] = useState(true)
    const [idleSpeed, setIdleSpeed] = useState(44)
    

    let intervalId

    const refresh = (finish = null) => {
      stingControlRepository.status()
      .then(({data}) => {
        data.position && setCurrentPos(data.position);
        setIdle(data.idle)
        setAutoIdle(data.autoIdle)
        setIdleMoveRight(data.idleMoveRight)
        setIdleMoveUp(data.idleMoveUp)
        setIdleSpeed(data.idleSpeed)

        if (typeof finish == 'function') {
          finish(data)
        }
      })
    }
    
    // const track = () => {
    //   if (currentPos.v == targetPos.v && currentPos.h == targetPos.h) {
    //     console.log('nothing to do')
    //     return
    //   }

    //   refresh()
    //   clearTimeout(timeoutId)
    //   timeoutId = setTimeout(track, TRACK_RATE)
    // }

    const updatePos = useCallback((axis, value) => {
      if (value == targetPos[axis]) return

      const newPos = { ...targetPos };
      newPos[axis] = value
      setTargetPos(newPos);

      stingControlRepository.move(MOTORS[axis], value)
      .then((data) => {
        // track()
      })
      
    }, [currentPos, targetPos])
    
    const step = useCallback((motor, direction) => {
      stingControlRepository.step(motor, direction)
      .then((data) => {
        console.log(data)
      })
    }, [])

    const toggleIdle = useCallback(() => {
      let req
      if (idle) {
        req = stingControlRepository.stop()
      } else {
        req = stingControlRepository.idleMove()
      }

      req.then((data) => {
        setIdle(!idle)
      })
    }, [idle])

    const startIdle = () => {
      stingControlRepository.idleMove().then((data) => {
        console.log(data);
      });
    }

    const stop = () => {
      stingControlRepository.stop().then((data) => {
        console.log(data)
      })
    }

    const reset = () => {
      stingControlRepository.reset_c().then((data) => {
        console.log(data);
      });
    }
    
    const toggleAutoIdle = useCallback(() => {
      let req

      if (autoIdle) {
        req = stingControlRepository.autoIdleOff()
      } else {
        req = stingControlRepository.autoIdleOn()
      }

      req.then((data) => {
        setAutoIdle(!autoIdle)
      })      
    }, [autoIdle])

    const toggleAxisIdle = useCallback((axis) => {
      let req
      const [_idleToggle, _setIdleToggle] = (axis == 'v') ? [idleMoveUp, setIdleMoveUp] : [idleMoveRight, setIdleMoveRight]

      if (_idleToggle) {
        req = stingControlRepository.toggleIdle(MOTORS[axis], 0)
      } else {
        req = stingControlRepository.toggleIdle(MOTORS[axis], 1)
      }

      req.then((data) => {
        _setIdleToggle(!_idleToggle);
      })
    }, [idleMoveUp, idleMoveRight])

    useEffect(() => {
      refresh((data) => setTargetPos(data.position))
      
      intervalId = setInterval(refresh, 2000)

      return () => {
        clearInterval(intervalId);
      }
    }, [])

    const renderButtons = () => (
      <div
        className="d-flex flex-column justify-content-between"
        style={{ clear: "both", minWidth: "200px" }}
      >
        <div className="d-flex flex-row justify-content-between">
          <a
            id="camera_control_reset"
            onClick={reset}
            className="btn btn-primary cnc_card-button mt-2"
          >
            Reset
          </a>
          <a
            id="camera_control_stop"
            onClick={stop}
            className="btn btn-danger cnc_card-button mt-2"
          >
            Stop
          </a>
          <a
            id="camera_control_idle"
            onClick={toggleIdle}
            className={classnames(
              "btn btn-success cnc_card-button mt-2",
              idle ? "btn-danger" : "btn-success"
            )}
          >
            Idle
          </a>
        </div>
        <div className="d-flex flex-column">
          <a
            id="camera_control_auto_idle_on"
            onClick={toggleAutoIdle}
            className={classnames(
              "btn cnc_card-button mt-2",
              autoIdle ? "btn-danger" : "btn-success"
            )}
          >
            Toggle Auto-Idle <strong>{autoIdle ? "Off" : "On"}</strong>
          </a>
          <a
            id="camera_control_idle_v"
            onClick={() => toggleAxisIdle("v")}
            className={classnames(
              "btn cnc_card-button mt-2",
              idleMoveUp ? "btn-danger" : "btn-success"
            )}
          >
            Toggle Idle V <strong>{idleMoveUp ? "Off" : "On"}</strong>
          </a>
          <a
            id="camera_control_idle_h"
            onClick={() => toggleAxisIdle("h")}
            className={classnames(
              "btn cnc_card-button mt-2",
              idleMoveRight ? "btn-danger" : "btn-success"
            )}
          >
            Toggle Idle H <strong>{idleMoveRight ? "Off" : "On"}</strong>
          </a>
        </div>
      </div>
    );

    return (
      <div className="mt-5">
        <div className="d-flex align-items-stretch flex-row">
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

          <div className="d-block" style={{ width: "100%", margin: "0 20px" }}>
            <div className="form-group">
              <label htmlFor="vRange" className="form-label">
                Vertical destination
              </label>
              <input
                type="range"
                className="form-range"
                id="vRange_dest"
                min={V_MIN}
                max={V_MAX}
                step={V_STEP}
                onChange={(e) => updatePos("v", e.target.value)}
                value={targetPos.v}
              />
            </div>
            <div className="form-group">
              <input
                type="range"
                className="form-range"
                id="vRange_pos"
                min={V_MIN}
                max={V_MAX}
                step={V_STEP}
                value={currentPos.v}
                disabled
              />
            </div>

            <div className="form-group">
              <label htmlFor="hRange" className="form-label">
                Horizontal destination
              </label>
              <input
                type="range"
                className="form-range"
                id="hRange_dest"
                min={H_MIN}
                max={H_MAX}
                step={H_STEP}
                onChange={(e) => updatePos("h", e.target.value)}
                value={targetPos.h}
              />
            </div>
            <div className="form-group">
              <input
                type="range"
                className="form-range"
                id="hRange_pos"
                min={H_MIN}
                max={H_MAX}
                step={H_STEP}
                value={currentPos.h}
                disabled
              />
            </div>
          </div>
          {renderButtons()}
        </div>
      </div>
    );
}