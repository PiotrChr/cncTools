import { AbstractApiRepository } from './abstractApiRepository';
import config from '../config';

export default class NotificationsRepository extends AbstractApiRepository {
    apiUrl = 'notifications/';

    async getStingDetectionNotifications() {
        return this.fetchJson(`${this.apiUrl}sting_detections/`);
    }

}