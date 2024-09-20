local entry = io.read()
local t = {}
for value in string.gmatch(entry, '[^%s]+') do
    table.insert(t, tonumber(value))
    
end
local avg = (t[1] * 2 + t[2] * 3 + t[3] * 4 + t[4])/10
print("Media: "..string.format('%.1f', avg))
if avg >= 7 then
    print('Aluno aprovado.')
elseif avg >= 5  then
    print("Aluno em exame.")
    local grade = io.read('n')
    avg = (avg + grade)/2
    print('Nota do exame: '..string.format('%.1f', grade))
    if avg >= 5 then
        print('Aluno aprovado.')
    else
        print('Aluno reprovado.')
    end
    print('Media final: '..string.format('%.1f', avg))
else
    print("Aluno reprovado.")
end