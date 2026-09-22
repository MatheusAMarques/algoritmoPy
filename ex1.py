def soma_imposto(taxa_imposto, custo):
    imposto = custo * taxa_imposto / 100
    return custo + imposto

custo = float(input("Digite o custo do produto: "))
taxa = float(input("Digite a taxa de imposto (%): "))
total = soma_imposto(taxa, custo)
print(f"somar_imposto(): {total:.2f}")