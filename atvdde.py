qntdAluno= input( "digite a quantidade de aluno:")
nomes = input("digite o nome os alunos:")
print("digite a nota dos alunos:")
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
print("digite a quantidade de faltas do aluno:")
faltas = int(input())
media = (n1+n2+n3+n4)/4
if media >= 8:
     print("O",nomes, "esta aprovado com:",media)
else:
      print("O",nomes,"esta reprovado e vai ter que fazer recuperação,por que tirou nota baixa",media)
print("digite quanto o", "aluno tirou na recuperação")
recuperacao = float(input())
if recuperacao >= 5:
      print("O aluno tirou",recuperacao ,"na recuperação")
else:
      print("o aluno não passou na recuperação,por que tirou",recuperacao)
if recuperacao < 5:
      print("O aluno esta reprovado por não alcançar a nota da recuperção e ficou com:",recuperacao)
elif faltas > 31:
      print("o aluno esta reprovado com",faltas)