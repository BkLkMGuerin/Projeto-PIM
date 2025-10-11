import collections
def media(a,b): #Esta função será usada para calcular a média das notas np1 e np2 do aluno
  notas_juntas = a+b
  resultado_media = notas_juntas/2
  return resultado_media

print('-=-=-=-='*5)
print('''   Selecione a matéria para o cadastro:
         [ 1 ] Português
         [ 2 ] Matemática
         [ 3 ] História
         [ 4 ] Ciências''')
print('-=-=-=-='*5)
saida = 0
while saida != 2:
  opcao_materia = int(input('Qual a matéria selecionada?: \n'))
  if opcao_materia == 1:#Esta é a condicional que abre as opções de cadastro na matéria de português 
    
      print('''O aluno já é cadastrado nesta matéria?: 
            [ 1 ] O aluno já é cadastrado (adcionar apenas as notas np1, np2)
            [ 2 ] Fazer o cadastro do aluno ''')
      cadastro_port = int(input('Qual opção selecionada: \n'))
      if cadastro_port == 2:
        nome_aluno_prt = str(input('Qual o nome e Sobrenome do aluno: \n'))
        ra_aluno_prt = str(input('Qual o RA do aluno: \n'))
        turma_aluno_prt = str(input('Qual a  turma do aluno: \n'))
        cadastro_aluno_port = (nome_aluno_prt + ',' + ra_aluno_prt + ',' + turma_aluno_prt) #Esta é a linha que será guardada todas as informações juntas do cadastro do aluno no arquivo da matéria
        with open('prt.txt','a') as f:
          f.write(cadastro_aluno_port + '\n')
        with open('prt.txt','r') as f:
          ler = f.read()
          print(ler)
      if cadastro_port == 2:
        print('final')

  elif opcao_materia == 2: #Esta é a condicional que abre as opções de cadastro na matéria de matemática 
    print('inicio matematica')

  elif opcao_materia == 3: #Esta é a condicional que abre as opções de cadastro na matéria de história
    print('inicio historia')

  elif opcao_materia == 4: #Esta é a condicional que abre as opções de cadastro na matéria de ciências
    print('inicio ciencias')
  else: #Caso a opção digitada seja diferente das opções disponíveis ela vai dar a opção de voltar ao loop e tentar outra opção ou então sair do sistema
    print('''Opção Inválida
          Gostaria de escolher outra opção ou sair do menu:
          [ 1 ] Escolher outra opção
          [ 2 ] Sair do menu ''')
    saida = int(input('Digite sua escolha: \n'))
    
  