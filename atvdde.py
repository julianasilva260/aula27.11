print("digite a quantidade de aluno:")
qntdaluno = int(input())
print("digite o nome dos alunos:")
nome = input()
print("digite a nota dos alunos:")
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
print("digite a quantidade de faltas do aluno:")
faltas = int(input())
media = (n1+n2+n3+n4)/4
if media >= 8:
     print("O aluno esta aprovado com:",media)
elif media >= 5:
      print("O aluno esta de recuperação com:",media)
elif media < 5:
      print("O aluno esta reprovado com:",media)
elif faltas > 31:
      print("o aluno esta reprovado com",faltas)