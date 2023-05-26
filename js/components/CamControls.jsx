import React, { useState, useEffect, useCallback } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import PropTypes from 'prop-types'
import classnames from 'classnames'
import StingControlRepository from '../repository/stingControlRepository'
import {
  selectAutoIdle,
  selectIdle,
  selectMoveRight,
  selectMoveUp,
  selectIdleSpeed,
  selectStingCurrentHAngle,
  selectStingCurrentVAngle,
  fetchStingStatus,
  toggleAxisIdle as toggleAxisIdleAction,
  toggleAutoIdle as toggleAutoIdleAction,
  stop as stopAction,
  reset as resetAction,
  toggleIdle as toggleIdleAction
} from '../state/stingControl'

const stingControlRepository = new StingControlRepository()

const DEFAULT_POS = { v: null, h: null }
const TRACK_RATE = 1000

const V_MAX = 115
const V_MIN = 75
const V_STEP = (V_MAX - V_MIN) / 10

const H_MAX = 180
const H_MIN = 0
const H_STEP = Math.ceil((H_MAX - H_MIN) / 40);

const MOTORS = {'h': 0, 'v': 1}

const CamControls = (props) => {
    const camera = props.camera
    const dispatch = useDispatch()
    const currentHAngle = useSelector(selectStingCurrentHAngle())
    const currentVAngle = useSelector(selectStingCurrentVAngle())
    const [targetPos, setTargetPos] = useState(DEFAULT_POS)
    const autoIdle = useSelector(selectAutoIdle())
    const idle = useSelector(selectIdle())
    const idleMoveRight = useSelector(selectMoveRight())
    const idleMoveUp = useSelector(selectMoveUp())
    const idleSpeed = useSelector(selectIdleSpeed())

    let intervalId

    const refresh = () => dispatch(fetchStingStatus())

    const updatePos = useCallback((axis, value) => {
      if (value == targetPos[axis]) return

      const newPos = { ...targetPos };
      newPos[axis] = value
      setTargetPos(newPos);

      stingControlRepository.move(MOTORS[axis], value)
      .then((data) => {
        // track()
      })
      
    }, [targetPos])
 
    const toggleIdle = useCallback(() => dispatch(toggleIdleAction(idle)), [idle])

    const stop = () => dispatch(stopAction())

    const reset = () => dispatch(resetAction())
    
    const toggleAutoIdle = () => dispatch(toggleAutoIdleAction())

    const toggleAxisIdle = (axis, currentValue) => dispatch(toggleAxisIdleAction(axis, currentValue))

    useEffect(() => {
      if (targetPos.v == null && currentVAngle !== null) {
        setTargetPos({h: currentHAngle, v: currentVAngle})
      }
    }, [currentHAngle, currentVAngle])

    useEffect(() => {
      intervalId = setInterval(refresh, 1000)

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
            onClick={() => toggleAxisIdle("v", idleMoveUp)}
            className={classnames(
              "btn cnc_card-button mt-2",
              idleMoveUp ? "btn-danger" : "btn-success"
            )}
          >
            Toggle Idle V <strong>{idleMoveUp ? "Off" : "On"}</strong>
          </a>
          <a
            id="camera_control_idle_h"
            onClick={() => toggleAxisIdle("h", idleMoveRight)}
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
                value={targetPos.v || 0}
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
                value={currentVAngle || 0}
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
                value={targetPos.h || 0}
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
                value={currentHAngle || 0}
                disabled
              />
            </div>
          </div>
          {renderButtons()}
        </div>
      </div>
    );
}

CamControls.propTypes = {
    refreshHandler: PropTypes.func
}

export default CamControls;