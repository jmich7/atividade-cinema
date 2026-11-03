def cadastrar_avaliacao():
    print("\n===== CADASTRAR AVALIAÇÃO =====")

    idade = int(input("Digite a idade do cliente: "))

    print("Escolha a avaliação:")
    print("1 - Ótimo")
    print("2 - Bom")
    print("3 - Regular")
    print("4 - Péssimo")

    opcao = input("Digite a opção: ")

    if opcao == "1":
        avaliacao = "Ótimo"
    elif opcao == "2":
        avaliacao = "Bom"
    elif opcao == "3":
        avaliacao = "Regular"
    elif opcao == "4":
        avaliacao = "Péssimo"
    else:
        print("Opção inválida!")
        return

    arquivo = open("avaliacoes.txt", "a", encoding="utf-8")
    arquivo.write(str(idade) + ";" + avaliacao + "\n")
    arquivo.close()

    print("Avaliação cadastrada com sucesso!")

def listar_avaliacoes():
    print("\n===== AVALIAÇÕES CADASTRADAS =====")

    try:
        arquivo = open("avaliacoes.txt", "r", encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()

        if len(linhas) == 0:
            print("Não existem avaliações cadastradas.")
        else:
            numero = 1

            for linha in linhas:
                dados = linha.strip().split(";")

                idade = dados[0]
                avaliacao = dados[1]

                print("Cliente", numero, "- Idade:", idade,
                      "- Avaliação:", avaliacao)

                numero = numero + 1

    except FileNotFoundError:
        print("Ainda não existe nenhuma avaliação cadastrada.")

def consultar_estatisticas():
    print("\n===== ESTATÍSTICAS DAS AVALIAÇÕES =====")

    try:
        arquivo = open("avaliacoes.txt", "r", encoding="utf-8")
        linhas = arquivo.readlines()
        arquivo.close()

        if len(linhas) == 0:
            print("Não existem avaliações cadastradas.")
        else:
            total = 0
            otimo = 0
            bom = 0
            regular = 0
            pessimo = 0

            idade_mais_velho = 0
            avaliacao_mais_velho = ""

            idade_mais_novo = 0
            avaliacao_mais_novo = ""

            for linha in linhas:
                dados = linha.strip().split(";")

                idade = int(dados[0])
                avaliacao = dados[1]

                total = total + 1

                if avaliacao == "Ótimo":
                    otimo = otimo + 1
                elif avaliacao == "Bom":
                    bom = bom + 1
                elif avaliacao == "Regular":
                    regular = regular + 1
                elif avaliacao == "Péssimo":
                    pessimo = pessimo + 1

                if total == 1:
                    idade_mais_velho = idade
                    avaliacao_mais_velho = avaliacao

                    idade_mais_novo = idade
                    avaliacao_mais_novo = avaliacao

                else:
                    if idade > idade_mais_velho:
                        idade_mais_velho = idade
                        avaliacao_mais_velho = avaliacao

                    if idade < idade_mais_novo:
                        idade_mais_novo = idade
                        avaliacao_mais_novo = avaliacao

            print("Total de respondentes:", total)
            print("Ótimo:", otimo)
            print("Bom:", bom)
            print("Regular:", regular)
            print("Péssimo:", pessimo)

            print("\nRespondente mais velho:")
            print("Idade:", idade_mais_velho, "anos")
            print("Avaliação:", avaliacao_mais_velho)

            print("\nRespondente mais novo:")
            print("Idade:", idade_mais_novo, "anos")
            print("Avaliação:", avaliacao_mais_novo)

    except FileNotFoundError:
        print("Ainda não existe nenhuma avaliação cadastrada.")

while True:
    print("\n===== SISTEMA DE AVALIAÇÃO DO CINEMA =====")
    print("1. Cadastrar avaliação")
    print("2. Listar avaliações")
    print("3. Consultar estatísticas")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_avaliacao()

    elif opcao == "2":
        listar_avaliacoes()

    elif opcao == "3":
        consultar_estatisticas()

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida! Tente novamente.")