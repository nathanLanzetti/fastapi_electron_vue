module.exports = {
  pluginOptions: {
    electronBuilder: {
      nodeIntegration: true, // enable use of node functions and ipcRenderer
      builderOptions: {
        extraFiles: [
          {
            from: "api/",
            to: "api/",
          },
          {
            from: "api_compiled/",
            to: "api_compiled/",
          },
          {
            from: "configs/",
            to: "configs/",
          },
        ],
      },
    },
  },
  transpileDependencies: ["vuetify"],
}
