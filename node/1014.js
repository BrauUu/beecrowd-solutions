var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let distance = Number(lines.shift());
let gas = Number(lines.shift());

console.log(`${(distance / gas).toFixed(3)} km/l`)