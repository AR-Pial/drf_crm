const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');

module.exports = {
    publicPath: "http://127.0.0.1:8080",
    outputDir: "./dist/",

    chainWebpack: config => {
        config.optimization.splitChunks(false)

        config.plugin('BundleTracker').use(BundleTracker, [
            {
              path: path.join(__dirname, './'),
              filename: 'webpack-stats.json'
            }
        ])

        config.resolve.alias.set('__STATIC__', 'static')

        config.devServer
            .host('127.0.0.1')
            .port(8080)
            .https(false)
            .headers({'Access-Control-Allow-Origin': ['\*']})
    }
};