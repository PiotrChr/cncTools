import { AbstractApiRepository } from "./abstractApiRepository";

export default class StingControlRepository extends AbstractApiRepository {
  apiUrl = "sting/";

  async idleMove() {
    return this.fetchJson(`${this.apiUrl}idle_move/`);
  }

  async autoIdleOn() {
    return this.fetchJson(`${this.apiUrl}auto_idle_on/`);
  }

  async autoIdleOff() {
    return this.fetchJson(`${this.apiUrl}auto_idle_off/`);
  }

  async reset() {
    return this.fetchJson(`${this.apiUrl}reset/`);
  }

  async stop() {
    return this.fetchJson(`${this.apiUrl}stop/`);
  }

  async step(motor, direction) {
    return this.fetchJson(`${this.apiUrl}step/${motor}/${direction}/`);
  }

  async move(motor, angle) {
    return this.fetchJson(`${this.apiUrl}move/${motor}/${angle}/`);
  }

  async idleSpeed(speed) {
    return this.fetchJson(`${this.apiUrl}idle_speed/${speed}/`);
  }

  async toggleIdle(motor, value) {
    return this.fetchJson(`${this.apiUrl}toggle_idle/${motor}/${value}`);
  }

  async status() {
    return this.fetchJson(`${this.apiUrl}status/`);
  }
}