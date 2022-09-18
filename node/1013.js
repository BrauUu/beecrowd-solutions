var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [a, b, c] = lines.shift().split(" ")

let greaterAB = (Number(a) + Number(b) + Math.abs(a - b)) / 2
let greaterABC = (greaterAB + Number(c) + Math.abs(greaterAB - c)) / 2

console.log(`${greaterABC} eh o maior`)