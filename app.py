

# aula pratica 1 dia 13-08-2026
# parte 1

a = 10
b = 20

# adição
soma = a + b
print(soma)

# subtração
subtracao = a - b
print(subtracao)

# multiplicacao
multiplicacao = a * b
print(multiplicacao)

# divisao com numero decimal
divisao = a / b
print(divisao)

# divisao com numero completo
divisaoCompleta = a // b
print(divisaoCompleta)

#  modulo / resto 
resto = a % b
print(resto)

# potencia
potencia = a ** b
print(potencia)

print("-" * 20)


# ------------ operação com string ---------------

primeiroNome = "Daniel"
secundoNome = "Monção"

# concatenação
nomeCompleto = primeiroNome + " " + secundoNome
print(nomeCompleto)

# repetição
repete = "hahahihi" * 20
print(f"e ele disse: {repete}")

print("-" * 5)

# Comparação
print("Expressoes de comparacao")

x = 10
y = 5

print(f"use '==' se x{x} for igual ao valor y {y} : {x==y}")
print(f"use '!=' se x{x} for diferente ao valor y {y} : {x!=y}")
print(f"use '<' se x{x} for menor ao valor y {y} : {x < y}")
print(f"use '>' se x{x} for maior ao valor y {y} : {x > y}")
print(f"use '<=' se x{x} for menor ou igual ao valor y {y} : {x <= y}")
print(f"use '>=' se x{x} for maior ou igual ao valor y {y} : {x >= y}")
print("skip" * 10)

# teste : comparação com valores string
primeiro = "treino"
segundo = "teste"

print(f"se o primeiro for igual '==' ,  o primeiro {primeiro} e o segundo {segundo} = {primeiro==segundo}")
print(f"se o primeiro for diferente '!=' ,  o primeiro {primeiro} e o segundo {segundo} = {primeiro!=segundo}")
print(f"se o primeiro for menor '<' ,  o primeiro {primeiro} e o segundo {segundo} = {primeiro < segundo}")
print(f"se o primeiro for maior ' > ' ,  o primeiro {primeiro} e o segundo {segundo} = {primeiro>segundo}")
print(f"se o primeiro for menor ou igual '<=' ,  o primeiro {primeiro} e o segundo {segundo} = {primeiro<=segundo}")
print(f"se o primeiro for maior ou igual '>=' ,  o primeiro {primeiro} e o segundo {segundo} = {primeiro>=segundo}")
print("skip" * 10)


# Operações Lógicas (AND, OR, NOT)

tem_dinheiro = True
tem_carro = False

pode_praia = tem_dinheiro and tem_carro
print(f"com o dinheiro e o carro voce consegue ir na praia ? {pode_praia}")
print("nao consegue porque nao tem carro, apenas dinheiro")
print("*" * 20)
pode_facul = tem_carro or tem_carro
print(f"com o dinheiro ou o carro voce pode ir a faculdade ? {pode_facul} ")
print("Consegue porque dentre eles , voce possui um pelo menos")
print("*" * 20)

nao_tem_carro = not tem_carro
print(f"nao tem carro ? {nao_tem_carro}")
print("retornou true porque realmente, voce nao tem carro")
print("-" * 10)
nao_tem_dinheiro = not tem_dinheiro
print(f"nao tem dinheiro ? {nao_tem_dinheiro}")
print("retornou falso porque voce possui dinheiro sim.")
print("*" * 25)

# ----------------------------- Exercicio 1 de equacao -------------------------------

# Descubra o número: “Um número somado ao seu dobro resulta em 36.” Qual é esse número?



# Um número somado ao seu dobro resulta em 36
# x + 2x = 36
# 3x = 36
# x = 36/3
# x = 12

x = 12
x_dobro = x * 2
resultado = x + x_dobro
print(f"O nemero somado ao seu dobro e {x}, somando com seu dobro {x_dobro} o resultado e {resultado}")
print("*" * 20)
# segundo método
y = 12
resultado = y + (y * 2)
print(f"o valor de y e {y}, somado com seu dobro o resultado e {y}") 
print("*" * 20)