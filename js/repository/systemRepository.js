import { AbstractApiRepository } from "./abstractApiRepository";

export default class SystemRepository extends AbstractApiRepository {
  apiUrl = "system/";

  async rebootSting() {
    return this.fetchJson(`${this.apiUrl}sting/reboot/`);
  }

  async detectorStatus() {
    return this.fetchJson(`${this.apiUrl}detector/status/`);
  }

  async stopDetector() {
    return this.fetchJson(`${this.apiUrl}detector/stop/`);
  }

  async startDetector() {
    return this.fetchJson(`${this.apiUrl}detector/start/`);
  }

  async restartDetector() {
    return this.fetchJson(`${this.apiUrl}detector/restart/`);
  }
}