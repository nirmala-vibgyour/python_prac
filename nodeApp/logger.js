const EventEmitter = require('events');

var url = "http://mylogger.io.log";

class Logger extends EventEmitter{
    log(message) {
        // Send an HTTP request
        console.log(message);
    
        // Raise an event
        this.emit('messageLogged', { id: 1, url: 'http://' });
    }
}


// setting as module.exports = log makes logger the function directly.
module.exports = Logger;