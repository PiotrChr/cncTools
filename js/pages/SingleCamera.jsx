import React, { useContext, useState, useEffect, useCallback } from 'react'
import PropTypes from 'prop-types'
import { default as SingleCameraC } from '../components/SingleCamera'


const SingleCamera = (props) => {
    return (
        <SingleCameraC camera={props.camera} />
    )
}

SingleCamera.propTypes = {
    camera: PropTypes.object
}

export default SingleCamera
