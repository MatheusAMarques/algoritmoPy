print("Exercicio 1 - Soma de dois valores")
print("-" * 15)
x = 8
y = 5
resultadoSoma = x + y
print(x)
print(y)
print(resultadoSoma)
print("-" * 15)
x = 4
y = 9
resultadoSoma = x + y
print(x)
print(y)
print(resultadoSoma)
print("-" * 15)

x = -3
y = 8
resultadoSoma = x + y
print(x)
print(y)
print(resultadoSoma)
print("-" * 15)

x = 0
y = 12
resultadoSoma = x + y
print(x)
print(y)
print(resultadoSoma)
print("-" * 15)

print("Exercicio 2  - media de duas notas")
print("-" * 15)

a = float(8)
b = float(6)
mediaNota = (a + b) / 2
print(f"primeira nota : {a}")
print(f"segunda nota : {b}")
print(f"media final : {mediaNota}")
print("-" * 15)

a = float(5.5)
b = float(7.5)
mediaNota = (a + b) / 2
print(f"primeira nota : {a}")
print(f"segunda nota : {b}")
print(f"media final : {mediaNota}")
print("-" * 15)

a = float(10)
b = float(9)
mediaNota = (a + b) / 2
print(f"primeira nota : {a}")
print(f"segunda nota : {b}")
print(f"media final : {mediaNota}")
print("-" * 15)


a = float(0)
b = float(4)
mediaNota = (a + b) / 2
print(f"primeira nota : {a}")
print(f"segunda nota : {b}")
print(f"media final : {mediaNota}")
print("-" * 15)

print("Exercicio 3 - Antecessor e sucessor")
print("-" * 15)

# a = int(input("Digite um numero: \n"))
a = 9
antecessor = a - 1
sucessor = a + 1
print(f"numero antecessor: {antecessor}")
print(f"numero selecionado: {a}")
print(f"numero sucessor: {sucessor}")
print("-" * 15)

a = 1
antecessor = a - 1
sucessor = a + 1
print(f"numero antecessor: {antecessor}")
print(f"numero selecionado: {a}")
print(f"numero sucessor: {sucessor}")
print("-" * 15)

a = 0
antecessor = a - 1
sucessor = a + 1
print(f"numero antecessor: {antecessor}")
print(f"numero selecionado: {a}")
print(f"numero sucessor: {sucessor}")
print("-" * 15)

a = -7
antecessor = a - 1
sucessor = a + 1
print(f"numero antecessor: {antecessor}")
print(f"numero selecionado: {a}")
print(f"numero sucessor: {sucessor}")
print("-" * 15)

print("Exercicio 4 - Dobro, triplo e metade")
print("-" *15)
x = int(input("digite um valor: "))
dobro = x * 2
triplo = x * 3
metade = x / 2
print(f"O valor digitado foi {x}")
print(f"O dobro do valor digitado é:  {dobro}")
print(f"O triplo do valor digitado é:  {triplo}")
print(f"A metade do valor digitado é:  {metade}")
print("-" * 15)

print("Exercicio 5 - Conversao de medidas")
print("-" * 15)
a = float(input("digite um valor"))
print(f"{a} metros;")
centimetros = a * 100
milimetros = centimetros * 10
print(f"{centimetros} cecntimetros;")
print(f"{milimetros} milimetros;")
print("-" * 15)

print("Exercicio 6 - Area e perimetros do retangulo")
print("-" * 15)
largura = float(input("informe o tamanho da largura: "))
altura = float(input("informe o tamanho da altura: "))
area = largura * altura
perimetro = 2 * (altura + largura)
print(f"Largura : {largura}")
print(f"Altura : {altura}")
print(f"Area : {area}")
print(f"Perimetro : {perimetro}")
print("-" * 15)

print("Exercicio 7 - Celsius para fahrenheit")
print("-" * 15)
celsius = int(input("informe a temperatura de celsius: "))
Fahrenheit = celsius * 9 / 5 + 32
print(f"Temperatura em C°: {celsius}")
print(f"Temperatura em F°: {Fahrenheit}")
print("-" * 15)

print("Exercicio 8 - Desconto no produto")
print("-" * 15)
preco = float(input("informe um preço: "))
desconto = preco * 0.10
precoFinal = preco - desconto
print(f"Preco : {preco}")
print(f"Desconto : {desconto}")
print(f"Preco final : {precoFinal}")
print("-" * 15)

print("Exercicio 9 - Aumento Salarial")
print("-" * 15)
salarioAtual = float(input("Digite seu salario atual: "))
aumento = salarioAtual * 0.15
novoSalario = salarioAtual + aumento
print(f"""
Salario atual : {salarioAtual};
Aumento: {aumento};
Novo salario : {novoSalario}
""")
print("Exercicio 10 - Salario com comissao")
print("-" * 15)
salarioFixo = float(input("Digite o salario fixo: "))
totalVendido = float(input("Digite o total de vendas: "))
comissao = totalVendido * 0.04
salarioTotal = salarioFixo + comissao
print(f"""
Salario fixo: {salarioFixo}
Total vendido{totalVendido}
Comissao: {comissao}
Salario total: {salarioTotal}
""")
print("-" * 15)

print("Exercicio 14 - Troca de valores")
print("-" * 15)

a = int(input("Digite um valor: "))
b = int(input("Digite um segundo valor"))

print(a)
print(b)
print("Ao contrario: ")
novoA = b
novoB = a 
print(novoA)
print(novoB)
print("-" * 15)

print("Exercicio 15 - Custo final da compra")
print("-" * 15)

precoUnitario = float(input("Digite o preco unitario: "))
quantidade = int(input("Digite a quantidade do produto: "))
frete = float(input("Digite a taxa de frete: "))
subtotal = precoUnitario * quantidade
total = subtotal + frete
print(f"Preco unitario: {precoUnitario}")
print(f"quantidade: {quantidade}")
print(f"taxa de frete: {frete}")
print(f"subtotal: {subtotal}")
print(f"total: {total}")