PORT_FILE = "portugues.txt"
MTM_FILE = "matematica.txt"
CIE_FILE = "ciencias.txt"
HST_FILE = "historia.txt"

def ler_txt(CAMINHO_ARQUIVO):
  '''Carrega o arquivo'''
  with open(CAMINHO_ARQUIVO,'r') as file:
    conteudo = file.read()

def escrever_txt(CAMINHO_ARQUIVO,aluno, nota1, nota2):
  with open(CAMINHO_ARQUIVO,'a') as file:
    file.write(f'{aluno}\n{nota1}\n{nota2}\n')
  
def menu_case(numero):
  match numero:
    case 1:
      print('A opção selecionada foi Português... \n')
      cadastro(PORT_FILE)
      return True
    case 2:
      print('A opção selecionada foi Matemática... \n')
      cadastro(MTM_FILE)
      return True
    case 3:
      print('A opção selecionada foi História... \n')
      cadastro(HST_FILE)
      return True
    case 4:
      print('A opção selecionada foi Ciências... \n')
      cadastro(CIE_FILE)
      return True
    case 0:
      print('Saindo do sistema...')
      return False
    case _:
      print('Opção escolhida inválida por favor selecione outra opção: \n')
      return True

def cadastro(CAMINHO_ARQUIVO):
  nome_aluno = str(input('Qual o nome e Sobrenome do aluno: \n'))
  ra_aluno = str(input('Qual o RA do aluno: \n'))
  turma_aluno = str(input('Qual a  turma do aluno: \n'))
  cadastro_aluno = (f'{nome_aluno}\n{ra_aluno}\n{turma_aluno}')
  notas_aluno = float(input('Qual a np1 do aluno: \n'))
  notas_aluno2 = float(input('Qual a np2 do aluno: \n'))

  escrever_txt(CAMINHO_ARQUIVO,cadastro_aluno,notas_aluno,notas_aluno2)
  print(f'O cadastro de {nome_aluno} foi feito: \n')
  print(f'{nome_aluno} {ra_aluno} {turma_aluno} {notas_aluno} {notas_aluno2}')

while True:
  print('-=-=-=-='*5)
  print('''   Selecione a matéria para o cadastro:
          [ 1 ] Português
          [ 2 ] Matemática
          [ 3 ] História
          [ 4 ] Ciências
          [ 0 ] Sair do menu''')
  print('-=-=-=-='*5)
  try:
      opcao_menu = int(input('Digite a opção selecionada (Ou [ 0 ] para fechar o menu): \n '))
  except ValueError:
    print('Entrada inválida. Digite um número')
    continue
  deve_continuar = menu_case(opcao_menu)
  if not deve_continuar:
    break
print('Programa encerrado.')
