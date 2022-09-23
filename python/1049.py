characteristic1 = input()
characteristic2 = input()
characteristic3 = input()

animals = {
    "aguia": ["vertebrado", "ave", "carnivoro"],
    "pomba": ["vertebrado", "ave", "onivoro"],
    "homem": ["vertebrado", "mamifero", "onivoro"],
    "vaca": ["vertebrado", "mamifero", "herbivoro"],
    "pulga": ["invertebrado", "inseto", "hematofago"],
    "lagarta": ["invertebrado", "inseto", "herbivoro"],
    "sanguessuga": ["invertebrado", "anelideo", "hematofago"],
    "minhoca": ["invertebrado", "anelideo", "onivoro"]
}

for animal in animals:
    count = 0
    if animals[animal][0] == characteristic1 or animals[animal][0] == characteristic2 or animals[animal][0] == characteristic3:
       count+= 1
    if animals[animal][1] == characteristic1 or animals[animal][1] == characteristic2 or animals[animal][1] == characteristic3:
       count+= 1
    if animals[animal][2] == characteristic1 or animals[animal][2] == characteristic2 or animals[animal][2] == characteristic3:
       count+= 1
    if count == 3:
        print(animal)