local word1 = io.read()
local word2 = io.read()
local word3 = io.read()

local animals = {
    vertebrado = {
        ave = {
            carnivoro = "aguia",
            onivoro = "pomba"
        },
        mamifero = {
            herbivoro = "vaca",
            onivoro = "homem"
        }
    },
    invertebrado = {
        inseto = {
            hematofago = "pulga",
            herbivoro = "lagarta"
        },
        anelideo = {
            hematofago = "sanguessuga",
            onivoro = "minhoca"
        }
    }
}

print(animals[word1][word2][word3])