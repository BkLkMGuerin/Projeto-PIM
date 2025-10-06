import collections

print(''' Selecione qual operação quer executar
      [ 1 ] Cadastro de aluno
      [ 2 ] Cadastro do aluno na matéria
      [ 3 ] Inserir notas
      [ 4 ] Cálculo de média''')
opt = int(input('Inserir opção:\n '))
lista_dados_alunos=[]

if opt==1: #Esta condicional determina o que fazer caso o usuário insira a opção 1 (Cadastro de aluno)
    while True:
        nome_aluno=str(input('Digite o nome completo do aluno: \n'))
        lista_dados_alunos.append(nome_aluno)
        ra_aluno=int(input('Digite o RA do aluno: \n'))
        lista_dados_alunos.append(ra_aluno)
        turma_aluno=str(input('Digite a turma do aluno: \n'))
        lista_dados_alunos.append(turma_aluno)
        sair=int(input('''Você gostaria de cadastrar outro aluno?
                       [ 1 ] SIM
                       [ 2 ] NÃO
                       Digite a opção'''))
        print(lista_dados_alunos)
        if sair==1:
            continue
        else:
            break
    
lista_mat=[]
lista_prt=[]
lista_cie=[]
lista_hst=[]

if opt==2:
    aluno=str(input('Digite seu nome e RA: \n')) #Esta condicional vai dar a oopção de qualmatéria o aluno faz parte e inserir ele na lista de matérias de qual for selecionada
    while True:    
        print('======' *7)
        print('''As matérias disponíveis são:
              [ 1 ] Mátematica
              [ 2 ] Ciências
              [ 3 ] Português
              [ 4 ] História''')
        print('======'*7)
        materia_aluno=int(input('Qual a matéria o aluno se inscreveu?:\n'))

        if materia_aluno==1:
            lista_mat.append(aluno)
        elif materia_aluno==2:
            lista_cie.append(aluno)
        elif materia_aluno==3:
            lista_prt.append(aluno)
        elif materia_aluno==4:
            lista_hst.append(aluno)
        else:
            print('Opção Inválida')
        sair2=int(input('''Você gostaria de cadastrar outra matéria?
                       [ 1 ] SIM
                       [ 2 ] NÃO
                       Digite a opção'''))
        print(f' mat{lista_mat}\n portugues{lista_prt} \n ciencias{lista_cie} \n história{lista_hst}\n')
        if sair2==1:
            continue
        else:
            break

            
