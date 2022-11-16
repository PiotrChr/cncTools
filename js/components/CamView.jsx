import React, { useEffect, useState, useCallback } from 'react'
import PropTypes from 'prop-types';
import { getCamFps, setCamFps } from '../context'


const CamView = (props) => {
    const [source, setSource] = useState(props.source)
    const [rotate, setRotate] = useState(props.rotate)
    const [fps, setFps] = useState(getCamFps(props.id))

    let intervalID;

    const refresh = () => {
        if (fps > 0) {
            setSource(props.source + "?hash=" + Date.now())
            // timeout = setTimeout(refresh, 1000 / fps)
        }
    }

    useEffect(() => {
      if (!props.dynamic) {
        clearInterval(intervalID)
        
        if (fps > 0) {
            intervalID = setInterval(refresh, 1000 / fps);
        }

        return () => clearInterval(intervalID);
      }
    }, [fps])
    
    const changeFps = useCallback((e) => {
        const value = e.target.value
        
        setCamFps(props.id, value)
        setFps(value)
    }, [])

    const onError = useCallback(() => {
        setSource("/static/img/camPlaceholder.png");
        setRotate(0)
    }, [fps]);

    return (
      <div className="single_cam_view" style={{ ...{}, ...props.style}}>
        <img
          style={{
            transform: "rotate(" + rotate + "deg)",
          }}
          className="card-img-top"
          src={source}
          onError={ onError }
        />
        <div style={{ position: "absolute", top: "10px" }}>
          <div className="form-group d-flex flex-row align-items-center form-group text-white">
            <label
              htmlFor={"fps_" + props.index}
              className="form-label"
              style={{ margin: "10px 20px" }}
            >
              <strong>FPS</strong>
            </label>
            <select
              className="form-select"
              aria-label="Refresh rate [FPS]"
              id={"fps_" + props.index}
              onChange={changeFps}
              value={fps}
            >
              <option value="0">0</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="5">5</option>
              <option value="10">10</option>
            </select>
          </div>
        </div>
      </div>
    );
}

CamView.propTypes = {
    fps: PropTypes.number,
    source: PropTypes.string,
    rotate: PropTypes.number,
    index: PropTypes.number,
    dynamic: PropTypes.bool,
    id: PropTypes.number,
    style: PropTypes.object
}

CamView.defaultProps = {
    fps: 0,
    rotate: 0,
    dynamic: false,
    style: {}
}

export default CamView
