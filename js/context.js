import React from 'react'
import Cookies from 'js-cookie'

const cookieCamPrefix = '_cam_fps_'

export const getCamFps = (cam) => {
    return Cookies.get(cookieCamPrefix + cam) ?? 0
}

export const setCamFps = (cam, value) => {
    Cookies.set(cookieCamPrefix + cam, value)
}

export const getCamConfigById = (cameras, camId) => {
    let cam = null
    cameras.forEach((camera) => {
      if (camera.id == camId) {
        cam = camera;
      }
    });

    return cam
}

export const GlobalContext = React.createContext();