import pandas as pd

df = pd.read_excel('analise.xlsx')

depositos_por_maquina = df['ID MÁQUINA'].value_counts()

total_pontos = df['PONTOS'].sum()

print("Depósitos por máquina:")
print(depositos_por_maquina)
print("\nTotal de pontos distribuídos:")
print(total_pontos)