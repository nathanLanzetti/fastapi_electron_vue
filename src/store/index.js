import Vue from "vue"
import Vuex from "vuex"
import { api } from "@/api.js"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    port: 0,
  },
  getters: {
    getPort: (state) => {
      return state.port
    },
  },
  mutations: {
    mutatePortFromFile(state, portNumber) {
      state.port = portNumber
    },
  },
  actions: {
    async setPortFromFile({ commit }) {
      const result = await api.getCurrentPort()
      commit("mutatePortFromFile", result)
    },
  },
  modules: {},
})
