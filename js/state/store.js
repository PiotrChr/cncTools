import { applyMiddleware, compose } from 'redux'
import { configureStore } from '@reduxjs/toolkit'
import thunkMiddleware from 'redux-thunk'
import { reducers, initialState } from './reducers'

const middleware = [thunkMiddleware]

const store = configureStore({
    reducer: reducers,
    middleware: middleware,
    devTools: process.env.NODE_ENV !== 'production',
    preloadedState: initialState
})


export default store