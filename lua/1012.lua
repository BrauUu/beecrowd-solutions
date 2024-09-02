local entry = io.read()
local t = {}
for value in string.gmatch(entry, "[^%s]+") do
    table.insert(t, value)

end
local A = t[1]
local B = t[2]
local C = t[3]

print("TRIANGULO: "..string.format("%.3f", A*C/2))
print("CIRCULO: "..string.format("%.3f", C^2 * 3.14159))
print("TRAPEZIO: "..string.format("%.3f", (A+B)*C/2))
print("QUADRADO: "..string.format("%.3f", B*B))
print("RETANGULO: "..string.format("%.3f", A*B))