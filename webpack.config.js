const path = require('path')

module.exports = {
  mode: "development",
  entry: {
    single: path.resolve(__dirname, 'js/entrypoints/', 'single.js'),
    index: path.resolve(__dirname, 'js/entrypoints/', 'index.js')
  },
  output: {
    path: path.resolve(__dirname, 'static/js/dist'),
    filename: '[name].js'
  },
  module: {
    rules: [
          {
            test: /\.(jsx|js)$/,
            resolve: {
              extensions: [".js", ".jsx"]
            },
            include: path.resolve(__dirname, 'js'),
            exclude: /node_modules/,
            use: [{
              loader: 'babel-loader',
              options: {
                presets: [
                  ['@babel/preset-env', {
                    "targets": "defaults"
                  }],
                  '@babel/preset-react'
                ]
              }
            }]
          }
        ]
  }
}