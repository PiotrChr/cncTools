import { AbstractApiRepository } from "./abstractApiRepository";

export default class SystemRepository extends AbstractApiRepository {
  apiUrl = "system/";

  async rebootSting() {
    return this.fetchJson(`${this.apiUrl}sting/reboot/`);
  }
}