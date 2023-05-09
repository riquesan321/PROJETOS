# Lê o número do produto digitado pelo usuário
numero_produto = input("Digite o número do produto: ")

# Abre o arquivo de produtos e procura pelo número do produto
produto_encontrado = False
with open("produtos.txt", "r") as arquivo_produtos:
    for linha in arquivo_produtos:
        partes = linha.strip().split("|")
        if partes[0] == numero_produto:
            # O produto foi encontrado na biblioteca
            produto_encontrado = True
            preco_produto = float(partes[1])
            break

# Exibe a mensagem apropriada dependendo se o produto foi encontrado ou não
if produto_encontrado:
    print(f"O produto {numero_produto} foi encontrado! O preço é R${preco_produto:.2f}.")
else:
    print(f"O produto {numero_produto} não está na biblioteca.")
