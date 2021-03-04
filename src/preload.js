// Not Used because settings modified in vue.config
const electron = require("electron")
const ipcRenderer = electron.ipcRenderer

window.ipcRenderer = ipcRenderer
