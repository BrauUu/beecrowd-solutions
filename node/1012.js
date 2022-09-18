//https://www.beecrowd.com.br/judge/pt/problems/view/1011

var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [a, b, c] = lines.shift().split(" ");

const PI = 3.14159

console.log(`TRIANGULO: ${(a * c / 2).toFixed(3)}`);
console.log(`CIRCULO: ${ (PI * Math.pow(c, 2)).toFixed(3)}`)
console.log(`TRAPEZIO: ${((parseFloat(a) + parseFloat(b)) * c / 2).toFixed(3)}`)
console.log(`QUADRADO: ${(b * b).toFixed(3)}`)
console.log(`RETANGULO: ${(a * b).toFixed(3)}`)