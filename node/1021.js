var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let value = lines.shift();

let count100Bills = parseInt(value / 100)
let remainingValue = parseFloat((value - count100Bills * 100).toFixed(2))
let count50Bills =  parseInt(remainingValue / 50)
remainingValue = parseFloat((remainingValue - count50Bills * 50).toFixed(2))
let count20Bills =  parseInt(remainingValue / 20)
remainingValue = parseFloat((remainingValue - count20Bills * 20).toFixed(2))
let count10Bills =  parseInt(remainingValue / 10)
remainingValue = parseFloat((remainingValue - count10Bills * 10).toFixed(2))
let count5Bills =  parseInt(remainingValue / 5)
remainingValue = parseFloat((remainingValue - count5Bills * 5).toFixed(2))
let count2Bills =  parseInt(remainingValue / 2)
remainingValue = parseFloat((remainingValue - count2Bills * 2).toFixed(2))

console.log('NOTAS:')
console.log(`${count100Bills} nota(s) de R$ 100.00`)
console.log(`${count50Bills} nota(s) de R$ 50.00`)
console.log(`${count20Bills} nota(s) de R$ 20.00`)
console.log(`${count10Bills} nota(s) de R$ 10.00`)
console.log(`${count5Bills} nota(s) de R$ 5.00`)
console.log(`${count2Bills} nota(s) de R$ 2.00`)

let count1Coins = parseInt(remainingValue / 1)
remainingValue = parseFloat((remainingValue - count1Coins).toFixed(2))
let count50Coins = parseInt(remainingValue / 0.5)
remainingValue = parseFloat((remainingValue - count50Coins * 0.5).toFixed(2))
let count25Coins = parseInt(remainingValue / 0.25)
remainingValue = parseFloat((remainingValue - count25Coins * 0.25).toFixed(2))
let count10Coins = parseInt(remainingValue / 0.10)
remainingValue = parseFloat((remainingValue - count10Coins * 0.10).toFixed(2))
let count05Coins = parseInt(remainingValue / 0.05)
remainingValue = parseFloat((remainingValue - count05Coins * 0.05).toFixed(2))
let count01Coins = parseInt(remainingValue / 0.01)
remainingValue = parseFloat((remainingValue - count01Coins * 0.01).toFixed(2))

console.log('MOEDAS:')
console.log(`${count1Coins} moeda(s) de R$ 1.00`)
console.log(`${count50Coins} moeda(s) de R$ 0.50`)
console.log(`${count25Coins} moeda(s) de R$ 0.25`)
console.log(`${count10Coins} moeda(s) de R$ 0.10`)
console.log(`${count05Coins} moeda(s) de R$ 0.05`)
console.log(`${count01Coins} moeda(s) de R$ 0.01`)