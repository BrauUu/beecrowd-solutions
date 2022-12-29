while True:
    try:
        string = input()
        
        if string == "":
            break
        
        if string == "esquerda":
            print("ingles")
        elif string == "direita":
            print("frances")
        elif string == "nenhuma":
            print("portugues")
        elif string == "as duas":
            print("caiu")
    except:
        break