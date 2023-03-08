# Pega os dados dos alunos
def nota_nome():
    nome = input("Coloque o nome do aluno: ")
    notas = []

    # pegas as notas
    for x in range(3):
        try:
            notas.append(float(input("Coloque a nota dele(a): ")))
        except:
            notas.append(0)
    return [nome, notas]


# faz o calculo da média das notas
def calculo_notas(notas, aluno):
    resultado = (notas[0]+notas[1]+notas[2])/3
    
    if resultado >= 7:
        print(aluno, "você está aprovado, você tirou ", round(resultado))
    else:
        print(aluno, "você reprovou, você tirou", round(resultado))

# Dicionario de alunos
Alunos = {}

# Pega o nome de cada aluno
for x in range(10):
    dados = nota_nome()
    Alunos.update({dados[0]: dados[1]})

# Lista de notas, registra as notas sendo nota1, nota2, nota3
notas = [[], [], []]

# loop do dicionario de alunos
for aluno in Alunos:
    # Calcula e printa as notas
    calculo_notas(Alunos[aluno], aluno)
    
    # Guarda os nomes e as notas nas listas
    notas[0].append([aluno, Alunos[aluno][0]])
    notas[1].append([aluno, Alunos[aluno][1]])
    notas[2].append([aluno, Alunos[aluno][2]])

# printa as notas e o nome dos alunos
for nota in notas:
    print(nota, "\n")
