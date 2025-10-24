PORT_FILE = "prt.txt"
MTM_FILE = "mtm.txt"
CIE_FILE = "cie.txt"
HST_FILE = "hst.txt"

def media(a,b): 
  '''Esta função será usada para calcular a média das notas np1 e np2 do aluno'''
  notas_juntas = a+b
  resultado_media = notas_juntas/2
  return resultado_media

def ler_txt(CAMINHO_ARQUIVO):
  '''Carrega o arquivo'''
  with open(CAMINHO_ARQUIVO,'r') as file:
    conteudo = file.read()

def escrever_txt(CAMINHO_ARQUIVO,aluno, media):
  with open(CAMINHO_ARQUIVO,'a') as file:
    file.write(f'{aluno}\nMédia {media}\n')
  
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
  cadastro_aluno = (f'Nome {nome_aluno}\nRA {ra_aluno}\nTurma {turma_aluno}')
  notas_aluno = float(input('Qual a np1 do aluno: \n'))
  notas_aluno2 = float(input('Qual a np2 do aluno: \n'))
  media_final = media(notas_aluno,notas_aluno2)
  escrever_txt(CAMINHO_ARQUIVO,cadastro_aluno,media_final)
  print(f'O cadastro de {nome_aluno} foi feito: \n')
  print(f'{nome_aluno} {ra_aluno} {turma_aluno} {media_final}')

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
