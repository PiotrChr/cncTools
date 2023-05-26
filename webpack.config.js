require('dotenv').config();
const path = require('path')
const webpack = require('webpack');

module.exports = {
  mode: "development",
  entry: {
    single: path.resolve(__dirname, 'js/entrypoints/', 'single.js'),
    cameras: path.resolve(__dirname, 'js/entrypoints/', 'cameras.js'),
    relays: path.resolve(__dirname, 'js/entrypoints/', 'relays.js'),
    window_openers: path.resolve(__dirname, 'js/entrypoints/', 'window_openers.js'),
    recordings: path.resolve(__dirname, 'js/entrypoints/', 'recordings.js'),
    index: path.resolve(__dirname, 'js/entrypoints/', 'index.js'),
    utils: path.resolve(__dirname, 'js/entrypoints/', 'utils.js'),
    notifications: path.resolve(__dirname, 'js/entrypoints/', 'notifications.js')
  },
  output: {
    path: path.resolve(__dirname, 'static/js/dist'),
    filename: '[name].js'
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': {
        'CNC_HOST': JSON.stringify(process.env.CNC_HOST)
      }
    })
  ],
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