
// function sayHello (name) {
//     console.log('Hello ' + name);
// }

// sayHello("Nirmala");
// console.log(module);

// to not make it be overriden
// const logger = require('./logger');

// console.log(logger)
// logger = 1;  causes error

// logger('message');

//  have built-in node modules: OS, Path, Process, QueryStrings, HTTP

// Path
const path = require('path');

var pathObj = path.parse(__filename);

console.log(pathObj)

// OS
const os = require('os');

var totalMemory = os.totalmem();
var freeMemory = os.freemem();

// console.log('Total Memory: ' + totalMemory);

console.log(`Total Memory: ${totalMemory}`);
console.log(`Free Memory: ${freeMemory}`);

//  File
const fs = require("fs");

// const file = fs.readdirSync('./')
// console.log(file);

fs.readdir('./', function(err, files) {
    if (err) console.log('Error', err);
    else console.log('Result', files);
});

// Event module
const EventEmitter = require('events');

const Logger = require('./logger');
// Logger object
const logger = new Logger();

// Register a listener
logger.on('messageLogged', (arg) => {  
    console.log('Listener called', arg)
});


logger.log('message');

// Raise an event to listen
// emitter.emit('messageLogged');

// event arguments whil raising an event
// emitter.emit('messageLogged', {id: 1, url: 'http://'});

// Raise: logging (data: message)

// HTTP
const http = require('http');

// server is an event emitter
const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Hello World');
        res.end();
    }

    if (req.url === '/api/courses') {
        res.write(JSON.stringify([1, 2, 3]));
        res.end();
    }
});

// server.on('connection', (socket) => {
//     console.log('New Connection!!');
// });

server.listen(3000);
console.log('Listening on port 3000...');

