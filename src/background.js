"use strict"

import { app, protocol, BrowserWindow } from "electron"
import { createProtocol } from "vue-cli-plugin-electron-builder/lib"
import installExtension, { VUEJS_DEVTOOLS } from "electron-devtools-installer"
const isDevelopment = process.env.NODE_ENV !== "production"
// const fs = require("fs")
// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([
  { scheme: "app", privileges: { secure: true, standard: true } },
])

async function createWindow() {
  // console.log(__dirname)
  const executablePath =
    "D:\\HELHA\\HELHA\\3BIG\\Stage\\vue_and_fastapi\\prototype\\proto_fastapi\\api_compiled\\main\\main.exe"

  // const port_file =
  //   "D:\\HELHA\\HELHA\\3BIG\\Stage\\vue_and_fastapi\\prototype\\proto_fastapi\\port_config.txt"

  // const executablePathBuild =
  //   "C:\\Users\\nath2\\AppData\\Local\\Programs\\proto_fastapi\\api_compiled\\main\\main.exe"
  // const port_fileBuild =
  //   "C:\\Users\\nath2\\AppData\\Local\\Programs\\proto_fastapi\\public\\port_config.txt"

  var exec = require("child_process").execFile
  console.log(process.env.VUE_APP_PORT_API)
  // process.env.VUE_APP_PORT_API = 1234
  console.log(process.env.VUE_APP_PORT_API)

  var fun = function() {
    console.log("fun() start")
    exec(executablePath, function(err, data) {
      console.log(err)
      console.log(data.toString())
    })
  }
  // Use fs.readFile() method to read the file
  fun()

  // Create the browser window.
  // process.env.PORT_API = 1543
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

/* IPCMAIN */
// ipcMain.on("port_config", (event, args) => {
//   console.log(event.sender)
//   console.log(args)
// })
