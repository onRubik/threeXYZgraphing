var unVar = require("underscore");
const fs = require('fs');

let data1 = fs.readFileSync('points.json');
let data2 = JSON.parse(data1);
//console.log(dataOut);


var jsonObject = data2

let x;
let y;
let z;

unVar.map( jsonObject, function(content) {
    unVar.map(content,function(data){
        console.log(unVar.allKeys(data));
        if(unVar.allKeys(data) === 'x'){
            console.log(unVar.values(data));
            x = unVar.values(data);
        }else if(unVar.allKeys(data) === 'y'){
            y = unVar.values(data);
        }else if(unVar.allKeys(data) === 'z'){
            z = unVar.values(data);
        }
        //console.log(x + ", " + y + ", " + z)
    })   
})

var async = {};
async.forEach = function(data2, cb) {
  var counter = 0,
    keys = Object.keys(data2),
    len = keys.length;
  var next = function() {
    if (counter < len) cb(data2[keys[counter++]], next);
  };
  next();
};

async.forEach(data2, function(val, next) {
  console.log("it did something");
  setTimeout(next, 100);
});

unVar.each(data2, function (value, key) {
    console.log(key);
});

console.log("all keys");
console.log(unVar.allKeys(data2));
console.log("");
console.log("keys");
console.log(unVar.keys(data2));