#Lista de produtos 

produto = [(' '), ('Pá', 123.00), ('Fósforo', 2.00), ('Chave', 5.00),
           ('Álcool', 12.00), ('Cerveja', 7.00), ('Coca', 13.00)]
produto.append(('Garrafa', 4.00))
produto.append(('Bola', 28.00))
produto.append(('Bolacha', 6.00))
produto.append(('Pão', 0.50))
produto.append(('Arroz', 20.00))

num_produto = range(1, len(produto))
produtos_selecionados = []

while True:
    print("Lista de produtos disponíveis:")
    for i in num_produto:
        if i == 0:
            print(f"{i} : {produto[i][0]} | Preço: R${produto[i][1]:.2f}")
        else:
            print(f"{i} : {produto[i][0]} | Preço: R${produto[i][1]:.2f}")

    escolher_produto = input('Digite o número do produto que você deseja ou digite "sair" para finalizar seu carrinho: ')

    if escolher_produto.isdigit():
        escolher_produto = int(escolher_produto)
        if 1 <= escolher_produto < len(produto):
            quantidade = True
            while quantidade:
                try:
                    quantidade_produto = int(input('Digite a quantidade desejada: '))
                    if quantidade_produto > 0:
                        quantidade = False
                        produtos_selecionados.append((produto[escolher_produto][0], produto[escolher_produto][1], quantidade_produto))
                        print(f'Produto Selecionado: {produto[escolher_produto][0]} | Preço: R${produto[escolher_produto][1]:.2f} | Quantidade: {quantidade_produto}')
                    else:
                        print('A quantidade deve ser maior que zero!')
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
    print(f"{produto_selecionado[0]} | Preço: R${produto_selecionado[1]:.2f} | Quantidade: {produto_selecionado[2]}")
    subtotal = produto_selecionado[1] * produto_selecionado[2]
    total += subtotal

print(f'Total: R${total:.2f}')

print('Caso tenha escolhido algum produto, para seguir em frente clique em "SEGUIR PARA O CARRINHO".')


