while true do
    local pass = io.read()
    if pass == "2002" then
        print('Acesso Permitido')
        break
    end
    print('Senha Invalida')
end