module.exports = {
  pluginOptions: {
    electronBuilder: {
      nodeIntegration: true,
      // preload: "src/preload.js",
      builderOptions: {
        extraFiles: [
          {
            from: "api/",
            // to:'./resources/api/'
            to: "api/",
          },
          {
            from: "databases/",
            // to:'./resources/api/'
            to: "databases/",
          },
          {
            from: "api_compiled/",
            // to:'./resources/api/'
            to: "api_compiled/",
          },
          {
            from: "configs/",
            // to:'./resources/api/'
            to: "configs/",
          },
        ],
      },
    },
  },
  transpileDependencies: ["vuetify"],
}
