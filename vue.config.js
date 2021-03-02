module.exports = {
  pluginOptions: {
    electronBuilder: {
      preload: "src/preload.js",
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
            from: "public/",
            // to:'./resources/api/'
            to: "public/",
          },
          // // {
          // //   from:'api/addon',
          // //   to:'api/addon'
          // // },
          // {
          //   from: "api/utils/stop_words_default.txt",
          //   to: "api/utils/stop_words_default.txt",
          // },
          // {
          //   from: "api/textblob_fr",
          //   to: "api/textblob_fr",
          // },
        ],
      },
    },
  },
  transpileDependencies: ["vuetify"],
}
