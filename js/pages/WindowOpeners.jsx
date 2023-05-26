import React from 'react'
import { useCallback, useEffect } from 'react'
import WindowOpener from '../components/WindowOpener'
import WindowOpenersRepository from '../repository/windowOpenersRepository'

const windowOpenersRepository = new WindowOpenersRepository()

const WindowOpeners = (props) => {

    const openTo = useCallback((openerId, value) => {
        windowOpenersRepository.openTo(openerId, value).then((data) => {
            console.log(data)
        })
    }, []);

    const stepDown = useCallback((openerId) => {
        windowOpenersRepository.stepDown(openerId).then((data) => {
          console.log(data);
        });
    }, []);

    const stepUp = useCallback((openerId) => {
        windowOpenersRepository.stepUp(openerId).then((data) => {
          console.log(data);
        });
    }, []);

    const open = useCallback((openerId) => {
        windowOpenersRepository.open(openerId).then((data) => {
          console.log(data);
        });
    }, []);

    const close = useCallback((openerId) => {
        windowOpenersRepository.close(openerId).then((data) => {
          console.log(data);
        });
    }, []);

    const refreshAll = () => {
        Promise.all(props.windowOpeners.map((opener) => windowOpenersRepository.status(opener.id)))
        .then((values) => {
            console.log(values)
        })
    }

    useEffect(() => {
        refreshAll()
    }, [])

    return (
        <div>
            { props.windowOpeners.map((opener) => (
                <WindowOpener
                    key={opener.id}
                    opener={opener}
                    onClose={ () => close(opener.id) }
                    onOpen={ () => open(opener.id) }
                />
            )) }
        </div>
    )
}

export default WindowOpeners