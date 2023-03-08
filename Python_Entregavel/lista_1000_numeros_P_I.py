def lista_1000():

    pares = []
    impares = []

    for y in range(1001):

        if (y % 2 == 0):
            pares.append(y)
        else:
            impares.append(y)

    return [pares, impares]

listas = lista_1000()

par = listas[0]
impar = listas[1]

print("Lista par: ", par, "\n")
print("Lista impar: ", impar, "\n")

