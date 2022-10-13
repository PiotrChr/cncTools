import React, { useEffect, useState, useContext } from 'react'
import { GlobalContext } from '../context';
import RecordingsRepository from '../repository/recordingsRepository'
import { default as RecordingsComponent } from "../components/Recordings";
import { getCamConfigById } from '../context'

const recordingsRepository = new RecordingsRepository()

const Recordings = (props) => {
    const [recordings, setRecordings] = useState(null)
    const context = useContext(GlobalContext)

    useEffect(() => {
        recordingsRepository.getRecStatus()
        .then(({data}) => {
            setRecordings(data.recordings)
        })
    }, [])

    return (
      <div>
        {recordings &&
          recordings.map(
            (recording, index) =>
              recording && (
                <div key={index} className="mb-5">
                  <h4>Camera: { getCamConfigById(context.cameras, recording.id).name } </h4>
                  <RecordingsComponent recordings={recording.recordings} />
                </div>
              )
          )}
      </div>
    );
}

export default Recordings
