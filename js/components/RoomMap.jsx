import React, { useCallback } from 'react'
import PropTypes from 'prop-types'
import RoomSVG from './RoomSVG'
import RangeSVG from './RangeSVG'
import cls from 'classnames'

const DEF_ANGLE = 30

const RoomMap = (props) => {
    const neutralAngle = 30 - props.defPosAngle
    const currentAngle = neutralAngle + (props.currentHAngle - 90)

    const doStyle = (index, zero) => Object.assign(
        {width: props.area[0], height: props.area[1], zIndex: index},
        zero && {position: 'absolute', top: '0px'}
    )

    return (
        <div style={ doStyle(1) } className={ cls('position-relative overflow-hidden', props.className) }>
            <div id="detector_map_bg" style={ doStyle(100, true) }/>
            <div id="detector_map_fg" style={ doStyle(101, true) }>
                <RoomSVG width={props.area[0]} height={props.area[1]} shape={props.shape} />
            </div>
            <div id="detector_map_items" style={ doStyle(102, true) }>
                <RangeSVG
                    className="detector_range"
                    size={ 600 }
                    rov={ props.rov }
                    style={{
                        position: 'absolute',
                        left: props.cameraPosition[0]+12,
                        bottom: props.cameraPosition[1]+12,
                        rotate: currentAngle+'deg'
                    }}/>
                <span
                    className="detector_cam"
                    style={{ position: 'absolute', left: props.cameraPosition[0], bottom: props.cameraPosition[1] }}
                />
            </div>
        </div>

    )
}

RoomMap.propTypes = {
    area: PropTypes.array,
    shape: PropTypes.array,
    cameraPosition: PropTypes.array,
    defPosAngle: PropTypes.number,
    currentHAngle: PropTypes.number,
    hRange: PropTypes.number,
    rov: PropTypes.number,
    className: PropTypes.string
}

RoomMap.defaultProps = {
    area: [100, 100],
    shape: [
        [0, 0],
        [0, 100],
        [100, 100]
        [100, 0]
    ],
    cameraPosition: [50, 50],
    currentHAngle: 90,
    defPosAngle: 90,
    hRange: 180,
    rov: 90
}

export default RoomMap