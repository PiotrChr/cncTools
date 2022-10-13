import { AbstractApiRepository } from "./abstractApiRepository";

class WindowOpenersRepository extends AbstractApiRepository {
  apiUrl = "window_openers/";

  async openWindow(openerId) {
    return this.fetchJson(`${this.apiUrl}${openerId}/open/`);
  }

  async closeWindow(openerId) {
    return this.fetchJson(`${this.apiUrl}${openerId}/close/`);
  }

  async stepUp(openerId) {
    return this.fetchJson(`${this.apiUrl}${openerId}/step_up/`);
  }

  async stepDown(openerId) {
    return this.fetchJson(`${this.apiUrl}${openerId}/step_down/`);
  }

  async status(openerId) {
    return this.fetchJson(`${this.apiUrl}${openerId}/status/`);
  }

  async openTo(openerId, value) {
    return this.fetchJson(`${this.apiUrl}${openerId}/open_to/${value}/`);
  }
}

export default WindowOpenersRepository