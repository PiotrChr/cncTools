import axios from 'axios';
import config from '../config';
import { stringifyParams } from '../utils';

export class AbstractApiRepository {
  apiBaseUrl = config.apiBaseUrl;

  timeout = 2

  getHeaders() {
    return {};
  }

  getUrl(path, params) {
    const query = stringifyParams(params);
    return `${config.apiHost}${config.apiUrl}${path}${query}`;
  }

  async fetchJson(path, params = {}) {
    const headers = this.getHeaders();

    try {
      const response = await axios.get(this.getUrl(path, params), { headers }, { timeout: this.timeout });
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  async postJson(path, data, params = {}) {
    const headers = this.getHeaders();

    try {
      const response = await axios.post(this.getUrl(path, params), data, { headers });
      return response.data;
    } catch (error) {
      this.handleError(error);
    }
  }

  async putJson(path, data, params = {}) {
    const headers = this.getHeaders();

    const query = stringifyParams(params);
    const url = `${this.apiBaseUrl}${path}${query}`;

    try {
      await axios.put(url, data, { headers });
    } catch (error) {
      this.handleError(error);
    }
  }

  handleError(error) {
    console.log('Repository error: ', error);
    throw error;
  }
}