// configure axios
import axios from "axios"
import store from "./store"
import { ipcRenderer } from "electron"

export const api = {
  getPort() {
    return store.getters.getPort
  },

  testPortConnection(portNumber) {
    let isSuccessful = false
    const result = axios
      .get(`http://localhost:${portNumber}/`)
      .then(() => {
        return !isSuccessful
      })
      .catch(() => {
        return isSuccessful
      })
    return result
  },

  async getCurrentPort() {
    const portNumber = ipcRenderer.sendSync("test")
    return portNumber
  },

  async queryUsers() {
    const result = axios
      .get(`http://localhost:${this.getPort()}/api/reddit/users/`)
      .then((response) => {
        return response.data
      })
    return result
  },

  async queryPosts() {
    const result = axios
      .get(`http://localhost:${this.getPort()}/api/reddit/posts/`)
      .then((response) => {
        return response.data
      })
    return result
  },

  async queryMonsters() {
    const result = axios
      .get(`http://localhost:${this.getPort()}/api/monsterhunter/monsters/`)
      .then((response) => {
        return response.data
      })
    return result
  },

  async queryWeapons() {
    const result = axios
      .get(`http://localhost:${this.getPort()}/api/monsterhunter/weapons/`)
      .then((response) => {
        return response.data
      })
    return result
  },
}
