var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [point1X, point1Y] = lines.shift().split(" ");
let [point2X, point2Y] = lines.shift().split(" ");

let distance = Math.sqrt(Math.pow((point2X - point1X), 2) + Math.pow((point2Y - point1Y), 2))

console.log(distance.toFixed(4))