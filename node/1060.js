var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let count = 0

for(let i = 0; i < 6;i++){
    let value = lines.shift();
    if(Number(value) > 0){
        count ++
    }
}

console.log(`${count} valores positivos`)