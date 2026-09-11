# def somar(numero1, numero2):
#     resultado = numero1 + numero2
#     return resultado

# def dividir(numero1, numero2):
#     resultado = numero1 / numero2
#     return resultado

# def multiplicar(numero1, numero2):
#     resultado = numero1 * numero2
#     return resultado

# def subtrair(numero1, numero2):
#     resultado = numero1 - numero2
#     return resultado

# soma = somar(5, 5)
# divisao = dividir(10, 2)
# multiplicacao = multiplicar(3, 4)
# subtracao = subtrair(10, 3)

# print("Soma:", soma)
# print("Divisão:", divisao)
# print("Multiplicação:", multiplicacao)
# print("Subtração:", subtracao)

# def calcular_media(lista_de_numero):
#     total = sum(lista_de_numero)
#     quantidade = len(lista_de_numero)
#     media = total / quantidade
#     return media

# media = calcular_media([1, 2, 3, 4, 5])
# print("Média:", media)

# def valida_string(palavra, maximo, minimo):
#     if len(palavra) > maximo:
#         return "A palavra é maior que o máximo permitido."
#     elif len(palavra) < minimo:
#         return "A palavra é menor que o mínimo permitido."
#     else:
#         return "A palavra está dentro do tamanho permitido."

# resultado_validacao = valida_string("Exemplo", 10, 3)
# print("Validação da palavra:", resultado_validacao)


def soma_imposto(taxa_imposto, custo):
    valor_final = custo + (custo * taxa_imposto / 100)
    return valor_final


custo = float(input("Digite o custo do item: "))
taxa_imposto = float(input("Digite a taxa de imposto (%): "))

resultado = soma_imposto(taxa_imposto, custo)

print(f"O valor final do produto é: {resultado:.2f}")
