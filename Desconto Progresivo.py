# Programa de desconto progreisssivo para loja
# Autor: Jéssica Dias
# Entrada
print("Bem-vindo ao Outlet da Jéssica Online!")
print("Por favor, insira as informações do pedido")
produto = input ("\nNome do produto: ")
preco = float(input("Preço do Produto:"))
if preco <= 0:
    print("\n❌ O preço deve ser maior que zero.")
    print( "\nTente novamente com um preço válido.")
    exit()
quantidade = int(input("Quantidade:"))    
if quantidade <= 0:
    print("\n❌ A quantidade deve ser maior que zero.")
    print( "\nTente novamente com uma quantidade válida.")
    exit()
# Processamento

total = preco * quantidade

if total >= 300:
    desconto = total * 0.15

elif total >= 200:
    desconto = total * 0.10

else:
    desconto = total * 0.05

valor_final = total - desconto

# Saída

print("\n🧾 RESUMO DO PEDIDO")
print(f"\nProduto: {produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Total da compra: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor Final: R$ {valor_final:.2f}")

print("\n Obrigado pela compra!")