import json
banco_dados = {}
opcao = 1
try:
    with open ("projeto-json", "r") as arquivo:
        banco_dados = json.load(arquivo)
except:
    print ("O arquivo não existe")
while opcao != 7:
    print("=" *60)
    print("Menu de opções: ")
    print("1- Inserir produto >>> ")
    print("2- Consultar produto por código >>> ")
    print("3- Consultar todos os produtos >>> ")
    print("4- Alterar o preço de um determinado produto >>> ")
    print("5- Aplicar um acréscimo ou um desconto em todos os produtos >>> ")
    print("6- Excluir registro de um produto >>> ")
    print("7- Sair do programa >>> ")
    print("=" *60)
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("=" *60)
        print("Inserir produto")
        codigo = input("Digite o código do produto >>> ") 
        nome = input("Digite o nome do produto >>> ")
        quantidade = int(input("Digite a quantidade desse produto >>> "))
        if quantidade > 0: #verificar disponibilidade
            disponivel = True
        else:
            disponivel = False
        preco = float(input("Digite o preço do produto >>> "))
        banco_dados[codigo] = {"Nome": nome, "Quantidade": quantidade, "Preco": preco, "Disponivel": disponivel,} #criando lista
        with open("projeto-json", "w") as arquivo: #abrir arquivo para escrita
            json.dump(banco_dados, arquivo, indent=4)
        print("Produto adicionado com sucesso! ")
    elif opcao == 2:
        print("=" *60)
        print("Consultar o produto por código")
        codigo = input("Digite o código do produto >>> ")
        if codigo in banco_dados:
                produto = banco_dados[codigo] #buscando produto pelo código
                print(f"O produto cadastrado com esse código é {produto}")
        else:
            print("Não tem produto cadastrado com esse código")
    elif opcao == 3:
        print("=" *60)
        print("Código\tNome\tQuantidade\tPreço\tDisponível")
        for chave in banco_dados:
            produto = banco_dados[chave]
            print (chave, end="\t")
            print (produto["Nome"],end="\t\t")
            print (produto["Quantidade"],end="\t")
            print (produto["Preco"],end="\t")
            print (produto["Disponivel"])
            #print(banco_dados)
    elif opcao == 4:
        print("=" *60)
        print("Alterar o preço de um produto")
        codigo = input("Digite o código do produto que deseja alterar o preço: ")
        if codigo in banco_dados: #se código estiver na lista 
            novo_preco = float(input("Digite o novo preço desse produto: "))
            banco_dados[codigo]["Preco"] = novo_preco #substituindo o preço
            with open("projeto-json", "w") as arquivo:
                json.dump(banco_dados, arquivo, indent=4) #salvando arquivo
            print("Preço atualizado com sucesso! ")
    elif opcao == 5:
        print("=" *60)
        print("Aplicar um acréscimo ou um desconto em todos os produtos")
        print ("1- Adicionar acréscimo aos produtos")
        print ("2- Desconto nos produtos")
        alterar = int(input("Deseja adicionar ou descontar? "))
        if alterar == 1: 
            porcentagem = float(input("Digite a porcentagem que deseja aumentar nos produtos >>> "))
            print("Preço alterado com sucesso!")
            for chave in banco_dados:               
                banco_dados[chave]["Preco"]= (banco_dados[chave]["Preco"] * (porcentagem / 100)) + banco_dados[chave]["Preco"] #buscando preço dentro da lista e acrescentando a porcentagem
        elif alterar == 2:
            porcentagem = float(input("Digite a porcentagem que deseja descontar nos produtos >>> "))
            print("Preço alterado com sucesso!") 
            for chave in banco_dados:
                banco_dados[chave]["Preco"]=banco_dados[chave]["Preco"] - (banco_dados[chave]["Preco"] * (porcentagem / 100)) #buscando preço dentro da lista e decontando a porcentagem     
        else:
            print("Opção inválida! ")     
        with open("projeto-json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4) #salvar alterações, acréscimo ou desconto
    elif opcao == 6:
        print("=" *60)
        print("Excluir registro de um produto")
        codigo = input("Digite o código que deseja excluir >>> ")
        if codigo in banco_dados:
            del banco_dados[codigo] #excluindo produto pelo código
            print("Produto excluído com sucesso! ")
        else:
            print("Não tem produto cadastrado com esse código")
        with open("projeto-json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
    elif opcao == 7:
        print("Saindo do programa ... ")
    else:
        print("Opção inválida, tente novamente")









