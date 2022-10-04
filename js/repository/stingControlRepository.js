import { AbstractApiRepository } from "./abstractApiRepository";

export default class SystemRepository extends AbstractApiRepository {
  apiUrl = "sting/";

  async idleMove() {
    return this.fetchJson(`${this.apiUrl}idle_move/`);
  }

  async idleIdleOn() {
    return this.fetchJson(`${this.apiUrl}auto_idle_on/`);
  }

  async idleIdleOff() {
    return this.fetchJson(`${this.apiUrl}auto_idle_off/`);
  }

  async reset() {
    return this.fetchJson(`${this.apiUrl}reset/`);
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
}