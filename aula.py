nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Bem-vindo(a) à aula de Python.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print(f"A soma de {numero1} e {numero2} é: {soma}")

numero3 = float(input("Digite a primeira nota: "))
numero4 = float(input("Digite a segunda nota: "))
media = (numero3 + numero4) /2
print(f"Sua média é: {media}")

numero1 = int(input("Digite um número: "))
antecessor = numero1 - 1
sucessor = numero1 + 1
print(f"O antecessor de {numero1} é: {antecessor}")
print(f"O sucessor de {numero1} é: {sucessor}")

numero1 = int(input("Digite um número: "))
dobro = numero1 * 2
triplo = numero1 * 3
metade = numero1 / 2
print(f"O dobro de {numero1} é: {dobro}")
print(f"O triplo de {numero1} é: {triplo}")
print(f"A metade de {numero1} é: {metade}")

metros = float(input("Digite um valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print(f"{metros} metros equivalem a {centimetros} centímetros.")
print(f"{metros} metros equivalem a {milimetros} milímetros.")

largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura em metros: "))
area = largura * altura
perimetro = 2 * (largura + altura)
print(f"A área do terreno é: {area} metros quadrados.")
print(f"O perímetro do terreno é: {perimetro} metros.")

celsius = float(input("Digite a temperatura desejada:" ))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura de {celsius}°C corresponde a {fahrenheit}°F.")

preco = int(input("Digite o preço do produto: "))
desconto = preco * 0.1
print(f"O preço do produto com 10% de desconto é: {preco - desconto}")

salario = float(input("Digite o salário do funcionário: "))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O novo salário do funcionário com 15% de aumento é: {novo_salario}")

salario = float(input("Digite o salário do funcionário: "))
total_vendas = float(input("Digite o total de vendas do funcionário: "))
comissao = total_vendas * 0.04
print(f"A comissão do funcionário é: {comissao}")
salario_total = salario + comissao
print(f"O salário total do funcionário é: {salario_total}")

numero = int(input(""))
if numero > 0:
        print(f"O número {numero} é positivo.")
else:
    print(f"O número {numero} é negativo.")

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print(f"O maior valor é {numero1}.")
elif numero1 < numero2:
    print(f"O maior valor é {numero2}.")
else:
    print(f"Os números {numero1} e {numero2} são iguais.")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

# Descobrindo o maior
if a >= b and a >= c:
    maior = a
else:
    if b >= c:
        maior = b
    else:
        maior = c

# Descobrindo o menor
if a <= b and a <= c:
    menor = a
else:
    if b <= c:
        menor = b
    else:
        menor = c


print()
print("Maior:", maior)
print("Menor:", menor)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é: {media}")
if media >= 7:
    print(f"Parabéns! Você foi aprovado com média {media}.")
else:
    print(f"Infelizmente, você foi reprovado com média {media}.")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é: {media}")


if media >= 7:
    print(f"Situação: Aprovado(a) com média {media}.")
elif media >= 5 and media < 7:
    print(f"Situação: Em exame com média {media}.")
else:
    print(f"Situação: Reprovado(a) com média {media}.")


idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Você não pode votar.")
elif idade >= 16 and idade < 18 or idade > 70:
    print("O voto é opcional para você.")
else:
    print("O voto é obrigatório para você.")
ano = int(input("Digite o ano que deseja verificar: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
else:
        print(f"O ano {ano} não é bissexto.")


preco = float(input("Digite o preço do produto: "))
opcao =int(input("Dinheiro ou Pix = 1 / Débito = 2 / Crédito a vista = 3 / Crédito parcelado = 4: "))
if opcao == 1:
    desconto = preco * 0.1
    preco_final = preco - desconto
    print(f"O preço final do produto com 10% de desconto é: {preco_final}")
elif opcao == 2:
    desconto = preco * 0.05
    preco_final = preco - desconto
    print(f"O preço final do produto com 5% de desconto é: {preco_final}")
elif opcao == 3:
    preco_final = preco
    print(f"O preço final do produto é: {preco_final}")
elif opcao == 4:
    acrescimo = preco * 0.08
    preco_final = preco + acrescimo
    print(f"O preço final do produto com 8% de acréscimo é: {preco_final}")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")


salario = float(input("Digite o salário do funcionário: "))
if salario <= 1500:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário com 15% de aumento é: {novo_salario}")
elif salario > 1500 and salario <= 3000:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário com 10% de aumento é: {novo_salario}")
elif salario > 3000:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    print(f"O novo salário do funcionário com 5% de aumento é: {novo_salario}")


peso = float(input("Digite o peso do paciente em kg: "))
altura = float(input("Digite a altura do paciente em metros: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f"ABAIXO DA FAIXA")
elif imc >= 18.5 and imc < 25:
    print(f"PESO NORMAL")
elif imc >= 25 and imc < 30:
    print(f"SOBREPESO")
else:
    print(f"OBESIDADE")


a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))


if a < b + c and b < a + c and c < a + b:
    print("Resultado: FORMAM UM TRIÂNGULO")
else:
    print("Resultado: NÃO FORMAM UM TRIÂNGULO")


a = float(input("Primeiro lado: "))
b = float(input("Segundo lado: "))
c = float(input("Terceiro lado: "))


if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("EQUILÁTERO")
    else:
        if a == b or a == c or b == c:
            print("ISÓSCELES")
        else:
            print("ESCALENO")
else:
    print("NÃO FORMA TRIÂNGULO")


valor_imovel = float(input("Digite o valor do imóvel: "))
salario = float(input("Digite o salário do comprador: "))
prazo = int(input("Digite o prazo de pagamento em anos: "))


prestacao_mensal = valor_imovel / (prazo * 12)
if prestacao_mensal <= salario * 0.3:
    print(f"Empréstimo aprovado! A prestação mensal será de R${prestacao_mensal:.2f}.")
else:
    print(f"Empréstimo negado! A prestação mensal de R${prestacao_mensal:.2f} excede 30% do salário do comprador.")


numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 e 5.")
elif numero % 3 == 0:
    print(f"O número {numero} é divisível por 3.")
elif numero % 5 == 0:
    print(f"O número {numero} é divisível por 5.")
else:
    print(f"O número {numero} não é divisível por 3 nem por 5.")


numero = float(input("Digite um número inteiro: "))
if numero >= 10 and numero <= 20:
    print(f"O número {numero} está entre 10 e 20.")
else:
    print(f"O número {numero} não está entre 10 e 20.")


numero = int(input("Digite um número inteiro: "))
if numero == 1:
    print("Segunda-feira")
elif numero == 2:
    print("Terça-feira")
elif numero == 3:
    print("Quarta-feira")
elif numero == 4:
    print("Quinta-feira")
elif numero == 5:
    print("Sexta-feira")
elif numero == 6:
    print("Sábado")
elif numero == 7:
    print("Domingo")
else:
    print("Número inválido. Por favor, digite um número entre 1 e 7.")


mes = int(input("Mês: "))
ano = int(input("Ano: "))

if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")
else:
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            print("29 dias")
        else:
            print("28 dias")
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("30 dias")
        else:
            print("31 dias")


idade = int(input("Digite a idade: "))
status = input("Estudante ou Não? (Digite 'S' para estudante e 'N' para não estudante): ")

if idade < 12 or status == 'S' or idade >= 60:
    valor_ingresso = 15
    print(f"O valor do ingresso é: R${valor_ingresso}")
else:
    valor_ingresso = 30
    print(f"O valor do ingresso é: R${valor_ingresso}")


    def valida_string(texto, minimo=1, maximo=100):
    tamanho = len(texto)
    if tamanho >= minimo and tamanho <= maximo:
        return True
    else:
        return False


def soma_imposto(taxa_imposto, custo):
    imposto = custo * taxa_imposto / 100
    valor_final = custo + imposto
    return valor_final


custo = float(input("Custo do item: "))
taxa = float(input("Taxa de imposto (%): "))

print(f"{soma_imposto}")

# total = soma_imposto(taxa, custo)
# print(f"Valor final: {total:.2f}")