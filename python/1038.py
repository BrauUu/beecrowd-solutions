item, quantity = input().split()
itemCod = int(item)
quantity = int(quantity)

itens = [{"item": 'Cachorro Quente', "price": 4.00},
         {"item": 'X-Salada', "price": 4.50},
         {"item": 'X-Bacon', "price": 5.00},
         {"item": 'Torrada simples', "price": 2},
         {"item": 'Refrigerante', "price":1.50}]

print(f'Total: R$ {(itens[itemCod - 1]["price"] * quantity):.2f}')