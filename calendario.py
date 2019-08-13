# JEITO FACIL

def dias (numero_digitado):
    return{
    1: "Domingo",
    2: "Segunda-feira", 
    3: "Terça-feira", 
    4: "Quarta-feira", 
    5: "Quinta-feira", 
    6: "Sexta-feira", 
    7: "Sábado"
    }[numero_digitado]


dia = int(input("Digite um número de 1 á 7: "))
    print(dias(dia))

### JEITO FACIL 2 

# dias_da_semana = {
#     1: "Domingo",
#     2: "Segunda-feira", 
#     3: "Terça-feira", 
#     4: "Quarta-feira", 
#     5: "Quinta-feira", 
#     6: "Sexta-feira", 
#     7: "Sábado"
# }

# dia = int(input("Digite um número de 1 á 7: "))

# try:                        # MODO PARA GERAR UMA EXCESSÃO CASO NÃO VALIDE
#     print(dias_da_semana[dia])

# except:                     # EXCESSÃO
#     print("XIIIIII, NÚMERO INVALIDO")


### JEITO DIFICIL E LONGO

# dia = int(input("Digite um número de 1 á 7: "))

# if dia == 1:
#     print("Hoje é domingo")
    
# elif dia == 2:
#     print("Hoje é segunda-feira") 

# elif dia == 3:
#     print("Hoje é terca-feira") 

# elif dia == 4:
#     print("Hoje é quarta-feira")       

# elif dia == 5:
#     print("Hoje é quinta-feira")       

# elif dia == 6:
#     print("Hoje é sexta-feira")  

# elif dia == 7:
#     print("Hoje é sábado")  

# else:
#     print("O número digitado é inválido") 
