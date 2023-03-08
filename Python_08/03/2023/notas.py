# Pedindo as notas
nota1 = float( input("Digite a nota1: "))
nota2 = float( input("Digite a nota2: "))
nota3 = float( input("Digite a nota3: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

print("A média desse estudante foi: ",media)