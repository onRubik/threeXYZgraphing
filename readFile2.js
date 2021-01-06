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
        unVar.map(data, function(content, data){
          //console.log(content);
          console.log(content);
          console.log(data);
        })
        // if(unVar.allKeys(data) === 'x'){
        //     console.log(unVar.values(data));
        //     x = unVar.values(data);
        // }else if(unVar.allKeys(data) === 'y'){
        //     y = unVar.values(data);
        // }else if(unVar.allKeys(data) === 'z'){
        //     z = unVar.values(data);
        // }
    })   
})

