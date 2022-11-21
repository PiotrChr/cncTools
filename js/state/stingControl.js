
import { data } from 'jquery'
import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { createSelector } from 'reselect'

import StingControlRepository from '../repository/stingControlRepository'
import SystemRepository from '../repository/systemRepository'

const stingControlRepository = new StingControlRepository()
const systemRepository = new SystemRepository()
// Selectors
export const app = (state) => state

export const selectStingCurrentHAngle = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.currentHAngle
    }
)

export const selectStingCurrentVAngle = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.currentVAngle
    }
)

export const selectTrackingStatus = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.isTracking
    }
)

export const selectIdle = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.idle
    }
)

export const selectAutoIdle = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.autoIdle
    }
)

export const selectMoveUp = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.idleMoveUp
    }
)

export const selectMoveRight = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.idleMoveRight
    }
)

export const selectIdleSpeed = () => createSelector(
    [app],
    (app) => {
        return app.stingControl.idleSpeed
    }
)


// Action names

export const STING_CONTROL_SET_STATUS = 'sting_control/status/set'
export const STING_CONTROL_SET_TRACKER_STATUS = 'sting_control/tracker_status/set'
export const STING_CONTROL_SET_AXIS_IDLE = 'sting_control/axis_idle/set'
export const STING_CONTROL_SET_AUTO_IDLE = 'sting_control/auto_idle/set'
export const STING_CONTROL_SET_IDLE = 'sting_control/auto_idle/set'

// Action creators

export const startIdle = () => dispatch => {
    
}

export const stopIdle = () => dispatch => {
    
}

export const toggleIdle = () => dispatch => {
    const idle = useSelector(selectIdle())
    let req

    if (idle) {
        req = stingControlRepository.stop()
    } else {
        req = stingControlRepository.idleMove()
    }

    req.then((data) => {
        dispatch({
            type: STING_CONTROL_SET_IDLE,
            value: !idle
        })
    })
}

export const toggleAutoIdle = () => dispatch => {
    const autoIdle = useSelector(selectAutoIdle())
    let req

    if (autoIdle) {
        req = stingControlRepository.autoIdleOff()
    } else {
        req = stingControlRepository.autoIdleOff()
    }

    req.then((data) => {
        dispatch({
            type: STING_CONTROL_SET_AUTO_IDLE,
            value: !autoIdle
        })
    })
}

export const toggleAxisIdle = (axis) => dispatch => {
    const idle = useSelector(axis == 'v' ? selectMoveUp() : selectMoveRight())
    const new_idle = idle ? 0 : 1

    stingControlRepository.toggleIdle(axis, new_idle)
    .then(() => {
        dispatch({
            type: STING_CONTROL_SET_AXIS_IDLE,
            axis: axis,
            value: new_idle
        })
    })
   
}

export const reset = () => dispatch => {
    stingControlRepository.reset_c().then((data) => {
        console.log(data);
    });
}

export const stop = () => dispatch => {
    stingControlRepository.stop().then((data) => {
        console.log(data)
    })
}

export const move = (motor, value) => dispatch => {
    stingControlRepository.move(motor, value)
    .then()
}

export const refreshTrackerStatus = () => dispatch => {
    systemRepository.detectorStatus()
    .then(({data}) => {
        const isTracking = data.status == 'active'

        dispatch({
            type: STING_CONTROL_SET_STATUS,
            isTracking
        })
    })
}

export const fetchStingStatus = () => dispatch => {
    stingControlRepository.status()
    .then(({data}) => {
        dispatch({
            type: STING_CONTROL_SET_STATUS,
            status: data
        })
    })
}

export const stingControlInitialState = {
    currentHAngle: null,
    currentVAngle: null,
    autoIdle: false,
    idle: false,
    idleMoveRight: true,
    idleMoveUp: true,
    idleSpeed: 44,
    isTracking: false
}

export const stingControlReducer = (state = stingControlInitialState, action) => {
    switch (action.type) {
        case STING_CONTROL_SET_STATUS:
            return ({...state, ...{
                currentVAngle: action.status.position.v,
                currentHAngle: action.status.position.h,
                autoIdle: action.status.autoIdle,
                idle: action.status.idle,
                idleSpeed: action.status.idleSpeed,
                idleMoveUp: action.status.idleMoveUp,
                idleMoveRight: action.status.idleMoveRight
            }})
        case STING_CONTROL_SET_AXIS_IDLE:
            if (action.axis == 'v') {
                state.idleMoveUp = action.value
            } else if (action.axis == 'h') {
                state.idleMoveRight = action.value
            }

            return state
        case STING_CONTROL_SET_AUTO_IDLE:
            return {...state, ...{idle: action.value}}
        case STING_CONTROL_SET_IDLE:
            return {...state, ...{autoIdle: action.value}}
        default:
            return state
    }
}