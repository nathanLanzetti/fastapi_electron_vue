// configure axios
import axios from "axios"
import store from "./store"
import { sendRequest } from "@/renderer.js"

// import fs from "fs"
// import path from "path"

// axios.get("/" + "port_config.text").then((response) => {
//   console.log(response.data)
//   //do anything you want with response.data (content of the file)
// })

export const api = {
  getPort() {
    return store.getters.getPort
  },

  async getCurrentPort() {
    sendRequest("port_config")
    // const port_fileBuild =
    //   "C:\\Users\\nath2\\AppData\\Local\\Programs\\proto_fastapi\\public\\port_config.txt"
    // const result = await axios.get("/" + "port_config.txt").then((response) => {
    // const result = await axios
    //   .get("static/port_config.txt")
    //   .then((response) => {
    //     console.log(response.data)
    //     console.log(process.env)
    //     console.log(store.getters.getPort)
    //     return response.data
    //   })
    // return result
    /* use `path` to create the full path to our asset */
    // const pathToAsset = path.join(__static, "public/port_config.txt")
    // console.log(pathToAsset)
    // const result = await axios
    //   .get("http://localhost:8080/port_config.txt")
    //   .then((response) => {
    //     console.log(response.data)
    //     console.log(process.env)
    //     console.log(store.getters.getPort)
    //     return response.data
    //   })
    // return result
    // return 0

    /* use `fs` to consume the path and read our asset */
    // const fileContents = fs.readFileSync(pathToAsset, "utf8")

    // console.log(fileContents)
    // return fileContents
  },

  async queryUsers() {
    const result = await axios
      .get(`http://localhost:${this.getPort()}/api/reddit/users/`)
      .then((response) => {
        return response.data
      })
    return result
  },

  async queryPosts() {
    const result = await axios
      .get(`http://localhost:${this.getPort()}/api/reddit/posts/`)
      .then((response) => {
        return response.data
      })
    return result
  },

  async queryMonsters() {
    const result = await axios
      .get(`http://localhost:${this.getPort()}/api/monsterhunter/monsters/`)
      .then((response) => {
        return response.data
      })
    return result
  },

  async queryWeapons() {
    const result = await axios
      .get(`http://localhost:${this.getPort()}/api/monsterhunter/weapons/`)
      .then((response) => {
        return response.data
      })
    return result
  },
}
