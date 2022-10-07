import { AbstractApiRepository } from './abstractApiRepository';
import config from '../config';

export default class RecordingsRepository extends AbstractApiRepository {
    apiUrl = 'rec/';

    async getRecStatus() {
        return this.fetchJson(`${this.apiUrl}status/`);
    }

    async getRecStatusForCam(cameraId) {
        return this.fetchJson(`${this.apiUrl}status/${cameraId}`);
    }

    async startRecording(cameraId) {
        return this.fetchJson(`${this.apiUrl}start/${cameraId}`);
    }

    async stopRecording(cameraId) {
        return this.fetchJson(`${this.apiUrl}stop/${cameraId}`);
    }

}