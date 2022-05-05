def map_recorder(_recorder):
    return {
        "camera": _recorder.camera,
        "name": _recorder.file_name,
        "recording_name": _recorder.recording_name,
        "started": _recorder.started_at,
        "thread_name": _recorder.name,
        "width": _recorder.width,
        "height": _recorder.height,
        "fps": _recorder.fps
    }
