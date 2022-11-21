
import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { createSelector } from 'reselect'

import NotificationsRepository from '../repository/notificationsRepository'

const notificationsRepository = new NotificationsRepository()
// Selectors
export const app = (state) => state

export const selectStingNotfications = () => createSelector(
    [app],
    (app) => {
        return app.notifications.sting
    }
)

// Action names

export const NOTIFICATIONS_STING_APPEND_ACTION = 'notification/sting/append'

// Action creators

export const notificationsStingAppend = () => dispatch => {
    notificationsRepository.getStingDetectionNotifications()
    .then(({data}) => {
        dispatch({
            type: 'notification/sting/append',
            notifications: data.notifications
        })
    })
}

export const notificationsInitialState = {
    sting: []
}

export const notificationsReducer = (state = notificationsInitialState, action) => {
    switch (action.type) {
        case NOTIFICATIONS_STING_APPEND_ACTION:
            state.sting = state.sting.concat(action.notifications)
            return state
       default:
            return state
    }
}