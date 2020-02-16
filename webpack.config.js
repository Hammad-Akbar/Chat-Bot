module.exports = {
    entry: "./scripts/Main.jsx",
    output: {
        path: __dirname,
        filename: "./static/script.js"
    },
    module: {
        rules: [
            { test: /\.css$/, loader: "style!css" },
            {
                test: /\.(js|jsx)$/,
                exclude: /(node_modules)/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react']
                }
            }
        ]
    },
    resolve: {
    extensions: ['.js', '.jsx'],
  }
};
