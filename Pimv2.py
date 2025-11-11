PORT_FILE = "portugues.txt"
MTM_FILE = "matematica.txt"
CIE_FILE = "ciencias.txt"
HST_FILE = "historia.txt"

def limite_nota(nota,max_nota):#Para limitar a entrada da nota entre 0 até o maximo escolhido(deixei max como váriavel para facilitação de manutenção do sistema)
  while True:
    try:
      leitura_nota= float(input(nota))
      if 0 <= leitura_nota <= max_nota:
        return leitura_nota
      else:
        print(f'Cadastro de nota inválida, a nota excedeu {max_nota}!')
    except ValueError:
      print('Cadastro inválido digite um número')

def limite_char(texto,max_char):#Vai definir o máximo de caracteres que o input pode receber(também variável para facilitar manutenção)
  while True:
    entrada_texto=str(input(texto))
    if len(entrada_texto) <= max_char:
      return entrada_texto
    else:
      print(f'Cadastro Inválido, limite de caracteres {max_char} alcançado!')

def escrever_txt(CAMINHO_ARQUIVO,aluno, nota1, nota2):#Escreve os dados na ordem correta para leitura em C
  with open(CAMINHO_ARQUIVO,'a',encoding='utf-8') as file:
    file.write(f'{aluno}\n{nota1} {nota2}\n')
  
def menu_case(numero):#Seletor das opções do menu
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
      return False #Retorno de false para sair do loop principal do menu 
    case _:#Caso o usuário escreva qualquer dado que não seja as opções dadas 
      print('Opção escolhida inválida por favor selecione uma opção existente: \n')
      return True

def cadastro(CAMINHO_ARQUIVO):#Função principal, faz o cadastro desde entrada de dados até a escrita no txt
  print('====='*5)#Indicador de início do processo para ser de mais fácil entendimento ao usuário
  print('INICIANDO CADASTRO')
  print('====='*5)
  nome_aluno = str(input('Qual o nome e Sobrenome do aluno: \n'))
  ra_aluno = limite_char('Qual o RA do aluno (máx 8 caracteres): \n',8)
  turma_aluno = limite_char('Qual a  turma do aluno (máx 6 caracteres): \n',6)
  cadastro_aluno = (f'{nome_aluno}\n{ra_aluno}\n{turma_aluno}')
  notas_aluno = limite_nota('Qual a np1 do aluno (máx nota 10): \n',10)
  notas_aluno2 = limite_nota('Qual a np2 do aluno (máx nota 10): \n',10)
  escrever_txt(CAMINHO_ARQUIVO,cadastro_aluno,notas_aluno,notas_aluno2)
  print(f'O cadastro de {nome_aluno} foi feito: \n')
  print('====='*5)#Indicador de finalização do processo
  print('CADASTRO FINALIZADO')
  print('====='*5)
  print(f'{nome_aluno}\n{ra_aluno}\n{turma_aluno}\n{notas_aluno}\n{notas_aluno2}')

while True:#Este é o bloco do menu principal 
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
