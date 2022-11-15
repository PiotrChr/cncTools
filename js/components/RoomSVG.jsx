import React from 'react'
import PropTypes from 'prop-types'

const RoomSVG = (props) => {
    const points = props.shape.reduce((acc, cur) => {
        return acc + cur.join(',') + ' '
    }, '')

    return (
        <svg height={ props.height } width={ props.width }>
            <polygon
                points={ points }
                style={{ stroke: 'black', strokeWidth: '5px', fill: 'none' }}
            />
        </svg>
    )
}


RoomSVG.propTypes = {
    width: PropTypes.number,
    height: PropTypes.number,
    shape: PropTypes.array
}

export default RoomSVG