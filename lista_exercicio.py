#Lista de produtos 

produtos = {
    1: ('Pá', 123.00),
    2: ('Fósforo', 2.00),
    3: ('Chave', 5.00),
    4: ('Álcool', 12.00),
    5: ('Cerveja', 7.00),
    6: ('Coca', 13.00),
    7: ('Garrafa', 4.00),
    8: ('Bola', 28.00),
    9: ('Bolacha', 6.00),
    10: ('Pão', 0.50),
    11: ('Arroz', 20.00)
}

produtos_selecionados = []

while True:
    print("Lista de produtos disponíveis:")
    for num_produto, produto_info in produtos.items():
        nome_produto, preco_produto = produto_info
        print(f"{num_produto} : {nome_produto} | Preço: R${preco_produto:.2f}")

    escolher_produto = input('Digite o número do produto que você deseja adicionar ao carrinho ou digite "sair" para finalizar: ')

    if escolher_produto.isdigit():
        escolher_produto = int(escolher_produto)
        if escolher_produto in produtos:
            quantidade = True
            while quantidade:
                try:
                    quantidade_produto = int(input('Digite a quantidade desejada: '))
                    if quantidade_produto > 0 and quantidade_produto <= 20:
                        quantidade = False
                        nome_produto, preco_produto = produtos[escolher_produto]
                        produtos_selecionados.append((escolher_produto, nome_produto, preco_produto, quantidade_produto))
                        print(f'Produto Selecionado: {nome_produto} | Preço: R${preco_produto:.2f} | Quantidade: {quantidade_produto}')
                    else:
                        print('A quantidade deve ser maior que zero e menor que 21 produtos!')
                        continue
                except ValueError:
                    print('Quantidade inválida!')
                    continue
        else:
            print('Você deve digitar um número válido que corresponda a um produto!')
            continue
    elif escolher_produto.lower() == "sair":
        break
    else:
        print('Ops, você só pode digitar os números que antecedem o nome dos produtos, também não é permitido letras ou símbolos!')
        continue

    continuar = True
    while continuar:
        opcao_continuar = input('Deseja escolher mais produtos? (Digite "S" para Sim ou "N" para Não): ')
        if opcao_continuar.lower() == "n":
            continuar = False
        elif opcao_continuar.lower() == "s":
            break
        else:
            print('Você deve digitar somente "S" ou "N", por favor tente novamente!')

print('Produtos selecionados:')
total = 0.0

for produto_selecionado in produtos_selecionados:
    num_produto, nome_produto, preco_produto, quantidade_produto = produto_selecionado
    print(f"{num_produto} - {nome_produto} | Preço: R${preco_produto:.2f} | Quantidade: {quantidade_produto}")
    subtotal = preco_produto * quantidade_produto
    total += subtotal

print(f'Total: R${total:.2f}')

# Remover produtos selecionados
while True:
    remover_produto = input("Digite o número do produto que você deseja remover ou digite 'sair' para finalizar: ")

    if remover_produto.isdigit():
        remover_produto = int(remover_produto)
        produto_removido = None
        for produto_selecionado in produtos_selecionados:
            num_produto, nome_produto, preco_produto, quantidade_produto = produto_selecionado
            if num_produto == remover_produto:
                produto_removido = produto_selecionado
                break

        if produto_removido is not None:
            print(f"Produto Selecionado: {nome_produto} | Preço: R${preco_produto:.2f} | Quantidade: {quantidade_produto}")
            remover_quantidade = int(input("Digite a quantidade que você deseja remover: "))

            if remover_quantidade > 0 and remover_quantidade <= quantidade_produto:
                if remover_quantidade == quantidade_produto:
                    produtos_selecionados.remove(produto_removido)
                else:
                    produtos_selecionados.append((num_produto, nome_produto, preco_produto, -remover_quantidade))
                print(f"Quantidade {remover_quantidade} do produto {nome_produto} removida com sucesso!")
            else:
                print("Quantidade inválida. Tente novamente!")
        else:
            print("Número de produto inválido. Tente novamente!")

    elif remover_produto.lower() == "sair":
        break
    else:
        print("Opção inválida. Tente novamente!")

print('Produtos selecionados atualizados:')
total = 0.0

for produto_selecionado in produtos_selecionados:
    num_produto, nome_produto, preco_produto, quantidade_produto = produto_selecionado
    print(f"{num_produto} - {nome_produto} | Preço: R${preco_produto:.2f} | Quantidade: {quantidade_produto}")
    subtotal = preco_produto * quantidade_produto
    total += subtotal

print(f'Total: R${total:.2f}')

