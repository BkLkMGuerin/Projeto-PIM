while True:#Cria um looping para quando o usuário rejeitar algo que faça resetar o programa ele volte para o 1°passo
    nome_idade = input("Digite seu nome e idade (Nessa ordem):\n")#*Etapa 1*
    nome = nome_idade.split()[0]#Split usado para pegar somente a primeira parte do input relacionado ao nome (se o usuário respeitar a orientação dada)
    print("Seja Bem-Vindo(a)", nome)
    print(nome,"Você concorda em usar seus dados", nome_idade,"para análise e estatistícas?")
    consent = input("s/n \n")#*Etapa 2*
    if consent == "n":
        continue#Voltar ao 1°passo se rejeitar
    elif consent == "s":#*Etapa 3*
        print(
        "\nTecnologia da Informação (TI) é o conjunto de atividades e soluções relacionadas\n"
        " ao uso de computadores, softwares, redes e outros recursos para processar, armazenar,\n "
        "proteger e transmitir informações. Ela é essencial para empresas, governos e pessoas\n"
        " na realização de tarefas, tomada de decisões e comunicação eficiente. "#Formatado para o código ser lido de uma forma mais fácil
    )
        while True:
            print("Gostaria de aprender mais sobre TI como pseudocódigo ou fluxograma?")
            interesse = input("s/n \n")#*Etapa 4*
            if interesse == "n":
                break
            elif interesse == "s":
                print("Gostaria de saber mais sobre pseudocódigo(p) ou fluxograma(f)")
                opcao = input("p/f \n")
                if opcao == "p":
                    print(
                    "\nPseudocódigo é uma forma de descrever algoritmos usando uma linguagem\n"
                    " simples e próxima da linguagem humana. Ele não segue a sintaxe de \n"
                    "nenhuma linguagem de programação específica, o que facilita o entendimento\n"
                    " da lógica por qualquer pessoa."
                )
                elif opcao == "f":
                    print(
                    "\nFluxograma é uma representação gráfica de um algoritmo ou processo,\n"
                    " utilizando símbolos como setas, retângulos e losangos. Ele ajuda a\n"
                    " visualizar o fluxo das etapas de forma clara, facilitando o entendimento\n"
                    " e a comunicação da lógica."
                )
                print(nome ,"Deseja sair do sistema? :")#*Etapa 5*
                sair = input("s/n \n")
                if sair == "s":
                    print("Obrigado pela participação")
                    break#Quebra o loop interno fazendo voltar a escolha entre os assuntos
                elif sair == "n":
                    continue#Segue o loop interno levando para o loop externo






