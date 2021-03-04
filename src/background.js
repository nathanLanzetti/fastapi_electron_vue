"use strict"

import { app, protocol, BrowserWindow, ipcMain } from "electron"
import { createProtocol } from "vue-cli-plugin-electron-builder/lib"
import installExtension, { VUEJS_DEVTOOLS } from "electron-devtools-installer"
import path from "path"
import { api } from "@/api.js"
import { execFile } from "child_process"

const isDevelopment = process.env.NODE_ENV !== "production"
const fs = require("fs")
// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([
  { scheme: "app", privileges: { secure: true, standard: true } },
])

async function createWindow() {
  let calcPath = ""
  if (process.env.NODE_ENV != "development") {
    calcPath = path.join(
      __dirname,
      "../",
      "../",
      "api_compiled",
      "main",
      "main.exe"
    )
  } else {
    calcPath = path.join(__dirname, "../", "api_compiled", "main", "main.exe")
  }
  console.log(calcPath)

  const executeApi = () => {
    console.log(calcPath)
    execFile(calcPath)
  }

  executeApi()

  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      // Use pluginOptions.nodeIntegration, leave this alone
      // See nklayman.github.io/vue-cli-plugin-electron-builder/guide/security.html#node-integration for more info
      nodeIntegration: process.env.ELECTRON_NODE_INTEGRATION,
    },
  })

  if (process.env.WEBPACK_DEV_SERVER_URL) {
    // Load the url of the dev server if in development mode
    await win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)
    if (!process.env.IS_TEST) win.webContents.openDevTools()
  } else {
    createProtocol("app")
    // Load the index.html when not in development
    win.loadURL("app://./index.html")
  }
}

// Quit when all windows are closed.
app.on("window-all-closed", () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== "darwin") {
    app.quit()
  }
})

app.on("activate", () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    // Install Vue Devtools
    try {
      await installExtension(VUEJS_DEVTOOLS)
    } catch (e) {
      console.error("Vue Devtools failed to install:", e.toString())
    }
  }
  createWindow()
})

// Exit cleanly on request from parent process in development mode.
if (isDevelopment) {
  if (process.platform === "win32") {
    process.on("message", (data) => {
      if (data === "graceful-exit") {
        app.quit()
      }
    })
  } else {
    process.on("SIGTERM", () => {
      app.quit()
    })
  }
}

/* ICP MAIN */
ipcMain.on("test", (event) => {
  let portFilePath = ""
  if (process.env.NODE_ENV != "development") {
    portFilePath = path.join(
      __dirname,
      "../",
      "../",
      "configs",
      "port_config.txt"
    )
  } else {
    portFilePath = path.join(__dirname, "../", "configs", "port_config.txt")
  }
  console.log(portFilePath)
  let portNumber = ""
  const intervalId = setInterval(() => {
    portNumber = fs.readFileSync(portFilePath, "utf-8")
    api.testPortConnection(portNumber).then((result) => {
      console.log(portNumber)
      if (result) {
        console.log(result)
        event.returnValue = portNumber
        clearInterval(intervalId)
      }
    })
  }, 1000)
})
