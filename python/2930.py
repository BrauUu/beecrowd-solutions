deliveredDate, deadline = input().split()
deliveredDate = int(deliveredDate)
deadline = int(deadline)

if deliveredDate > deadline:
    print("Eu odeio a professora!")
elif deliveredDate + 3 <= deadline:
    print("Muito bem! Apresenta antes do Natal!")
elif deliveredDate + 3 > deadline:
    print("Parece o trabalho do meu filho!")
    deliveredDate += 2
    if deliveredDate < 24:
        print("TCC Apresentado!")
    else:
        print("Fail! Entao eh nataaaaal!")