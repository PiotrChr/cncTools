import React from 'react'
import Cookies from 'js-cookie'

const cookieCamPrefix = '_cam_fps_'

export const getCamFps = (cam) => Cookies.get(cookieCamPrefix + cam) ?? 0

export const setCamFps = (cam, value) => {
    Cookies.set(cookieCamPrefix + cam, value)
}

export const GlobalContext = React.createContext();