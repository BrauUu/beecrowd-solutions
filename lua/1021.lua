local value = io.read('n')

local count100 = value // 100
value = string.format("%.2f", value - count100 * 100)
local count50 = value // 50
value = string.format("%.2f", value - count50 * 50)
local count20 = value // 20
value = string.format("%.2f", value - count20 * 20)
local count10 = value // 10
value = string.format("%.2f", value - count10 * 10)
local count5 = value // 5
value = string.format("%.2f", value - count5 * 5)
local count2 = value // 2
value = string.format("%.2f", value - count2 * 2)

local count1 = value // 1
value = string.format("%.2f", value - count1 * 1)
local count05 = value // 0.5
value = string.format("%.2f", value - count05 * 0.5)
local count025 = value // 0.25
value = string.format("%.2f", value - count025 * 0.25)
local count01 = value // 0.1
value = string.format("%.2f", value - count01 * 0.1)
local count005 = value // 0.05
value = string.format("%.2f", value - count005 * 0.05)
local count001 = value // 0.01
value = string.format("%.2f", value - count001 * 0.01)

print('NOTAS:')
print(string.format("%d", count100).." nota(s) de R$ 100.00")
print(string.format("%d", count50).." nota(s) de R$ 50.00")
print(string.format("%d", count20).." nota(s) de R$ 20.00")
print(string.format("%d", count10).." nota(s) de R$ 10.00")
print(string.format("%d", count5).." nota(s) de R$ 5.00")
print(string.format("%d", count2).." nota(s) de R$ 2.00")
print('MOEDAS:')
print(string.format("%d", count1).." moeda(s) de R$ 1.00")
print(string.format("%d", count05).." moeda(s) de R$ 0.50")
print(string.format("%d", count025).." moeda(s) de R$ 0.25")
print(string.format("%d", count01).." moeda(s) de R$ 0.10")
print(string.format("%d", count005).." moeda(s) de R$ 0.05")
print(string.format("%d", count001).." moeda(s) de R$ 0.01")
