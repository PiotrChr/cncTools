import { notificationsReducer, notificationsInitialState } from './notifications'
import { stingControlReducer, stingControlInitialState } from './stingControl'


export const reducers = {
    notifications: notificationsReducer,
    stingControl: stingControlReducer
}

export const initialState = {
    notifications: notificationsInitialState,
    stingControl: stingControlInitialState
}

export default reducers
