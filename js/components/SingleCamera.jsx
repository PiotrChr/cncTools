import React, { useContext, useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import { GlobalContext } from '../context'
import Recordings from './Recordings'
import RecStatus from './RecStatus'
import CamControls from './CamControls'
import CamView from './CamView'
import CamDetector from './CamDetector'
import RecordingsRepository from '../repository/recordingsRepository'
import StingControlRepository from '../repository/stingControlRepository'
import { useCallback } from 'react'

const recordingsRepository = new RecordingsRepository()
const stingControlRepository = new StingControlRepository()

const SingleCamera = (props) => {
    const [recordings, setRecordings] = useState(null)
    const [recStatus, setRecStatus] = useState(null)
    const [currentPos, setCurrentPos] = useState({ v: 0, h: 0 })
    const context = useContext(GlobalContext)

    const { camera } = props
    const rotate = camera.rotate ?? 0

    let intervalId;

    const refresh = (data) => {
        data.position && setCurrentPos(data.position);
    }

    useEffect(() => {
        fetchStatus()

        if (recStatus) {
            intervalId = setInterval(fetchStatus, 1000)
        }

        return () => {
            clearInterval(intervalId)
        }
    }, [])

    const fetchStatus = () => {
        recordingsRepository.getRecStatusForCam(camera.id).then(({data}) => {
          setRecordings(data.recordings.recordings);
          setRecStatus(data.status);
        });
    }

    const startRecording = useCallback(() => {
        recordingsRepository.startRecording(camera.id)
        setTimeout(fetchStatus, 1000)
    }, [])

    const stopRecording = useCallback(() => {
        recordingsRepository.stopRecording(camera.id);
        setTimeout(fetchStatus, 500);
    })

    const removeRecording = useCallback((camera, recording) => {
        recordingsRepository.removeRecording(camera, recording);
        setTimeout(fetchStatus, 1000);
    }, []);

    const playRecording = useCallback(() => {

    }, [])

    return (
      <div className="row">
        <div className="col-12">
          <div className="card cam_card">
            <CamView
              source={camera.source}
              rotate={rotate}
              index={camera.id}
              dynamic={camera.type == "dynamic"}
              id={camera.id}
            />
            <div className="card-body">
              <h5 className="card-title cnc_card-title">{camera.name}</h5>
              <div
                className="d-flex  flex-column justify-content-between"
                style={{ clear: "both" }}
              >
                <div>
                  <a href="/sec" className="btn btn-primary cnc_card-button">
                    Back
                  </a>
                  {recStatus ? (
                    <a
                      onClick={stopRecording}
                      className="btn btn-danger cnc_card-button"
                    >
                      Stop Recording
                    </a>
                  ) : (
                    <a
                      onClick={startRecording}
                      className="btn btn-success cnc_card-button me-5"
                    >
                      Start Recording
                    </a>
                  )}
                </div>

                {camera.move && <CamControls camera={camera} refreshHandler={refresh} />}
              </div>
            </div>
          </div>
        </div>
        {camera.detector &&
            <CamDetector
                camera={ camera }
                className='mt-5 mb-5'
            />}
        {recStatus && <RecStatus {...recStatus} />}
        {recordings && (
          <Recordings
            recordings={recordings}
            cameraId={camera.id}
            onPlay={playRecording}
            onRemove={removeRecording}
          />
        )}
      </div>
    );
}

SingleCamera.propTypes = {
    camera: PropTypes.object
}

export default SingleCamera