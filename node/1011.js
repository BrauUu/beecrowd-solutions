//https://www.beecrowd.com.br/judge/pt/problems/view/1011

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let radius = parseInt(lines.shift());
const PI = 3.14159;

console.log(`VOLUME = ${((4/3) * PI * Math.pow(radius, 3)).toFixed(3)}`);