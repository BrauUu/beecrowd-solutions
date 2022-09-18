n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

avg = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

print(f'Media: {avg:.1f}')

if avg >= 7:
    print('Aluno aprovado.')
elif avg >= 5 and avg < 7:
    print('Aluno em exame.')
    nExam = float(input())
    print(f'Nota do exame: {nExam:.1f}')
    newAvg = (avg + nExam) / 2
    if newAvg >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {newAvg:.1f}')
else:
    print('Aluno reprovado.')