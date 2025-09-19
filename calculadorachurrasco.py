# crie um program que calcule a quantidade de bebidas e de carne para a 
#a  organização de um churrasco 
#etapas da resolução
# 1) solicitar o número de convidados 
# 2) criar uma função para calcular a quantidade total de bebidas 
#3) criar uma função para calcular a quantidade  total de carnes
#4) apresentar o resultado com os valores de total de carne e de bebida

convidados = int(input("Digite o número de convidados: "))

def calcular_bebidas(convidados, consumo_por_pessoa_ml =800, volume_garrafa_litro = 2.23):
    total_ml = convidados * consumo_por_pessoa_ml
    total_litro=total_ml/100

    garrafa = int(total_litro//volume_garrafa_litro)
    if total_litro % volume_garrafa_litro >0:
        garrafa += 1
    return total_litro, garrafa

resultado=calcular_bebidas(convidados)
print(resultado)

def calcular_carne(convidados,consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama # informa a quantidade total de carne em gramas
    total_kg= total_gramas /1000 #transformando o valor total em gramas por quilo
    return total_kg

litros, garradas = calcular_bebidas(convidados)
carne_kg= calcular_carne(convidados)

print('\n___Quantidade total para o churrasco___')
print(f'Numero de convidados: {convidados} ')
print(f'Refrigerantes necessarios: {litros:.2f} litros.')
print(f'Garrafas de 2,5L: {carne_kg:.2f} Kg.')
