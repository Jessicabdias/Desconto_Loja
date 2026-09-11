
## 🛍️Calculadora de Desconto Progressivo
🐍 Python | 📚 Projeto de estudo | 🧮Calculadora para desconto progressivo

>Um programa desenvolvido em **Python** para calcular automaticamente o desconto de uma compra de acordo com o valor total do pedido.

Este projeto foi criado como prática no meu curso técnico de **Desenvolvimento de Sistemas**, com foco nos conceitos básicos de programação e na construção de um programa organizado e funcional.


## 🎯 Objetivo

O programa recebe o **nome do produto, preço e quantidade**, calcula o valor total da compra e aplica um desconto progressivo conforme a faixa de valor.

Além disso, o programa possui validações para evitar preços e quantidades menores ou iguais a zero.

## ⚙️ Como funciona

O programa segue o fluxo:

**Entrada → Processamento → Saída**

O programa recebe o nome do produto, preço e quantidade, calcula o valor total da compra e aplica um desconto progressivo de acordo com as porcentagens definidas pelo professor para o exercício.
### 📥 Entrada

O usuário informa:

* Nome do produto
* Preço do produto
* Quantidade

### 🧮 Processamento

O programa:

1. Calcula o total da compra.
2. Verifica qual faixa de desconto deve ser aplicada.
3. Calcula o valor do desconto definido para o exercício.
4. Calcula o valor final da compra.

### 📤 Saída

Ao final, o programa apresenta um resumo contendo:

* Produto
* Preço unitário
* Quantidade
* Total da compra
* Valor do desconto
* Valor final


## 💰 Regras de desconto

| Valor total da compra      | Desconto |
| Até R$ 199,99              |       5% |
| De R$ 200,00 até R$ 299,99 |      10% |
| A partir de R$ 300,00      |      15% |


## 💻 Exemplo de execução

```text
Bem-vindo ao Outlet da Jéssica Online!
Por favor, insira as informações do pedido

Nome do produto: Camiseta
Preço do Produto:100
Quantidade:3
```

### Resultado

```text
🧾 RESUMO DO PEDIDO

Produto: Camiseta
Preço: R$ 100.00
Quantidade: 3
Total da compra: R$ 300.00
Desconto: R$ 45.00
Valor Final: R$ 255.00

Obrigado pela compra!
```

---

## 🛠️ Tecnologias utilizadas

* 🐍 **Python**
* 💻 **VS Code**
* 🔗 **Git e GitHub**
* ⌨️ `input()`
* 🖨️ `print()`
* 🔢 Conversão de dados com `float()`
* ✨ F-strings para formatação da saída

---

## 👩‍💻 Autora

**Jéssica Dias**

Projeto desenvolvido para prática de **Python e lógica de programação**.