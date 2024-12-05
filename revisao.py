alunos = []
escolha_menu =int(input("Escolha uma opção do menu:"))#variavel que guarda qual escolha do usuário
if escolha_menu == 1: #se a escolha for para realizar  
    #ler entradas do usuario
    cont = 0 #variavel que controla a reptição
    print("Digite a quantidade de alunos:")
    escolha_usuario = int(input()) #variavel que guarda quantas vezes o codigo vai rodar
    #lista que guardara todos os alunos cadrastados
    while cont < escolha_usuario:
        print("Digite o nome do aluno(a)")
        nome = input() #armazenar o nome do aluno
        print("Digite as nota do aluno(a)")
        n1 = float(input()) #4 notas do aluno
        n2 =float(input())
        n3 =float(input())
        n4 =float(input()) 
        print("Digite a quantidade de faltas do aluno(a)")
        faltas = int(input())
        #calculo da media 
        media = (n1+n2+n3+n4)/4
        print(media)
        #LÓGICA DA SITUAÇÃO
        if faltas > 31:
            situacao = nome,"esta reprovado por faltas"
        elif media >= 8:
            situacao = nome,"esta aprovado"
        elif media >= 5: #recuperação
            recuperacao = float(input("Digite a nota do aluno(a) da recuperação:")) #ler a nota da prova de recuperação
            if recuperacao >= (10-media):
                situacao= "esta aprovado(a) na recuperação"
            else:
                situacao = "esta reprovado(a) na recuperação"
        else:
            situacao = "esta reprovado(a) por media"

    #enviar os dados do aluno para a lista (alunos)
    alunos.append([nome,faltas,media,situacao])
    cont += 1
    #relatorio
print(alunos)