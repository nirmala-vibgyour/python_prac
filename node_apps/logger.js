
var url = "http://mylogger.io.log";

function log(message) {
    // Send an HTTP request
    console.log(message);
}

// setting as module.exports = log makes logger the function directly.
module.exports = log;