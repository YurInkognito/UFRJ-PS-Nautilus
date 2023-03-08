def primos():
    primos_lista = [2]
    for y in range(2,1001):
        count = 0
        for x in primos_lista:
            if y % x == 0:
                count += 1
        if count == 0:
            primos_lista.append(y)
    return primos_lista;

lista_primos = primos()

resultado = 0
for primos in lista_primos:
    resultado += primos

print(resultado)
