#ler entradas do usuario
cont = 0 #variavel que controla a reptição
print("Digite a quantidade de alunos:")
escolha_usuario = int(input()) #variavel que guarda quantas vezes o codigo vai rodar
while cont < escolha_usuario:
    print("Digite o nome do aluno(a)")
    nome = input() #armazenar o nome do aluno
    print("Digite as nota do aluno(a)")
    n1 = float(input()) #4 notas do aluno
    n2 =float(input())
    n3 =float(input())
    n4 =float(input()) 
    faltas = int(input())
    #calculo da media 
    media = (n1+n2+n3+n4)/4
    #LÓGICA DA SITUAÇÃO
    if faltas > 31:
        situacao = nome,"esta reprovado por faltas"
    elif media >= 8:
        situacao = nome,"esta aprovado"
    elif media >= 5: #recuperação
         recuperacao = float(input()) #ler a nota da prova de recuperação
         if recuperacao >= (10-media):
            situacao= nome,"esta aprovado(a) na recuperação"
         else:
          situacao = nome,"esta reprovado(a) na recuperação"
    else:
        situacao = nome,"esta reprovado(a) por media com a nota"
    #relatorio
    print("RELATÓRIO DO ALUNO(A)",nome)
    print("nome:",nome)
    print("notas:",n1,n2,n3,n4)
    print("faltas:",faltas)
    print("situação do aluno(a):",situacao)
    cont = cont+1