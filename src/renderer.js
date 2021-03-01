import { ipcRenderer } from "electron"
// import fs from "fs"
// import path from "path"

export function sendRequest(requestName) {
  console.log(requestName)
  if (requestName == "port_config") {
    ipcRenderer.send("port_config", "hello")
    // ipcRenderer.once("port_config", (event, arg) => {
    //   console.log(`EVENT : ${event}`)
    //   console.log(`ARGS : ${arg}`)
    //   const data = fs.readFileSync("../port_config.txt")
    //   console.log(data)
    // })
  }
}
