import React from 'react'
import PropTypes from 'prop-types'

const RangeSVG = (props) => {
    const { rov, size, ...rest } = props
    const base = 2 * size * Math.tan(1/2 * (rov * Math.PI / 180))
    const points = [
        [base/2, 0],
        [base, size],
        [0, size]
    ].reduce((acc, cur) => acc + cur.join(',') + ' ', '')

    return (
        <div { ...rest } >
            <svg height={ size } width={ base }>
                <linearGradient id="range_gradient" x1="0%" x2="100%" y1="100%" y2="60%">
                    <stop className="range_gradient_main-stop" offset="0%" />
                    <stop className="range_gradient_alt-stop" offset="70%" />
                </linearGradient>
                <polygon
                    points={ points }
                    style={{ stroke: 'none', fill: 'url(#range_gradient)' }}
                />
            </svg>
        </div>
    )
}


RangeSVG.propTypes = {
    rov: PropTypes.number,
    size: PropTypes.number
}

export default RangeSVG