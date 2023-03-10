# 
#   Baixe tabulate pelo pip (pip install tabulate)
#   tabulate: Modulo para mostrar como tabela
#
from tabulate import tabulate

class AUVs:
    # Guarda todos os AUVs
    lista_auvs = []

    def __init__(self, nome: str, ano: int, thursters: int, team: int):
        
        auv = self.AUV(nome,  ano, thursters, team)
        self.lista_auvs.append(auv)
    
    def print_auv(self):
        
        tabela = [["Nome", "Ano", "Thursters", "Team"]]
        for auv in self.lista_auvs:
            tabela.append([auv.nome, auv.ano, auv.thursters, auv.team])
        
        print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid", showindex="always"))
   
    def print_auv_especifico(self):
        
        try:
            decisao = int(input("Digite o index do AUV que você deseja obter informações: "))
        except:
            print("Você digitou algo errado, tente novamente. ")
        
        try:
            
            auv = self.lista_auvs[decisao]
            
            tabela = [["Nome", "Ano", "Thursters", "Team"]]
            tabela.append([auv.nome, auv.ano, auv.thursters, auv.team])

            print(tabulate(tabela, headers="firstrow", tablefmt="fancy_grid"))
        except:
            print("Esse AUV não existe")
    
    def escolha(self):
        
        decisao = input("Digite 'pa' para mostrar todos os AUVs ou digite 'ps' para algum AUV em especifico: ")
        
        if decisao == "pa":
            self.print_auv()
        
        elif decisao == "ps":
            self.print_auv_especifico()
        
        else:
            print("Esse comando não existe. ")

    class AUV:
        def __init__(self, nome: str, ano: int, thursters: int, team: int):
            self.nome = nome
            self.ano = ano
            self.thursters = thursters
            self.team = team

#Instancia um objeto da Classe "AUVs"
auvs = AUVs(nome='AUV Lua', ano=2022, thursters=8, team=42)
auvs = AUVs(nome='AUV BrHue', ano=2020, thursters=6, team=35)

auvs.escolha()