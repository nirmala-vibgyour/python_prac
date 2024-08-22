
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
const emitter = new EventEmitter();

// Register a listener
emitter.on('messageLogged', function() {
    console.log('Listener called')
})

// Raise an event to listen
emitter.emit('messageLogged');



