import React, { useEffect, useState, useCallback } from 'react'
import PropTypes from 'prop-types';
import { getCamFps, setCamFps } from '../context'


const CamView = (props) => {
    const [source, setSource] = useState(props.source)
    const [fps, setFps] = useState(getCamFps(props.id))
    let timeout;

    const refresh = () => {
        setSource(props.source + "?hash=" + Date.now())
        timeout = setTimeout(refresh, 1000 / props.fps)
    }

    useEffect(() => {
      if (props.dynamic) {
        if (timeout) {
            clearTimeout(timeout)
        }
        if (props.fps > 0) {
            refresh()
        }
      }
    }, [fps])
    
    const changeFps = useCallback((e) => {
        console.log(e.target)
        setCamFps(e.target.value)
        setFps(e.target.value)
    }, [])

    return (
        <div className="single_cam_view">
            <img style={{ transform: "rotate(" + props.rotate + "deg)"}} className="card-img-top" src={ source } alt="Card image cap" />
            <div style={{ position: 'absolute', top: '10px' }}>
                <div className="form-group d-flex flex-row align-items-center form-group text-white">
                    <label htmlFor={ "fps_"+ props.index } className="form-label" style={{margin: "10px 20px"}}><strong>FPS</strong></label>
                    <select className="form-select" aria-label="Refresh rate [FPS]" id={ "fps_" + props.index } onChange={changeFps} value={fps}>
                        <option value="0">0</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="5">5</option>
                        <option value="10">10</option>
                    </select>
                </div>
            </div>
            
        </div>        
    )
}

CamView.propTypes = {
    fps: PropTypes.number,
    source: PropTypes.string,
    rotate: PropTypes.number,
    index: PropTypes.number,
    dynamic: PropTypes.bool,
    id: PropTypes.string
}

CamView.defaultProps = {
    fps: 0,
    rotate: 0,
    dynamic: false
}

export default CamView
