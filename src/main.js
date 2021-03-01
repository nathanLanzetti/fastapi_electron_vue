import Vue from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import vuetify from "./plugins/vuetify"

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app")

// execFile(executablePath)

// console.log(process.env.PORT_API)

// const result = require("dotenv").config()

// if (result.error) {
//   throw result.error
// }

// console.log(result.parsed)

// console.log(process.env.PORT_API)
console.log(process.env)
// const exec = require("child_process").execFileSync
// const executablePath =
//   "D:\\HELHA\\HELHA\\3BIG\\Stage\\vue_and_fastapi\\prototype\\proto_fastapi\\api_compiled\\main\\main.exe"

// // child(executablePath, function(err, data) {
// //   if (err) {
// //     console.error(err)
// //     return
// //   }

// //   console.log(data.toString())
// // })
// exec(executablePath)

// const util = require("util")
// const execFile = require("child_process").execFile

// execFile(executablePath)
// require("child_process").execFile("../api_compiled/main/main.exe")
// const executablePath =
//   "D:\\HELHA\\HELHA\\3BIG\\Stage\\vue_and_fastapi\\prototype\\proto_fastapi\\api_compiled\\main\\main.exe"

// execFile(executablePath)
