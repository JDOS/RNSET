import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('join_RNS.csv', sep=';', encoding='cp1252')  

print(df.head(3))
df['Município'] = df['Município'].astype(str)

top_10 = df.nlargest(10, 'Acidentes')

bars = plt.bar(top_10['Município'], top_10['Acidentes'], color='skyblue')
plt.title('10 Municípios com maiores números de acidentes')
plt.xlabel('Município')
plt.ylabel('Acidentes')
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade
plt.tight_layout()  # Ajusta o layout

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}'.replace(',', '.'), ha='center', va='bottom', fontsize=8)

plt.show()


top_10 = df.nlargest(10, 'Acidentes')
# Criando o gráfico
plt.figure(figsize=(12, 6))
x = np.arange(len(top_10['Município']))  # A posição das barras

# Plotando as barras da população
bars1 = plt.bar(x, top_10['População'], label='População', color='skyblue', alpha=0.7)

# Plotando as barras de acidentes sobrepostas
bars2 = plt.bar(x, top_10['Acidentes'], label='Acidentes', color='orange', alpha=0.7)

# Adicionando título e rótulos
plt.title('Ranking das 10 Cidades com Maior Número de Acidentes e suas Populações')
plt.xlabel('Município')
plt.ylabel('Quantidade')
plt.xticks(x, top_10['Município'], rotation=45)  # Rotaciona os rótulos do eixo x
plt.legend()

# Adicionando os números acima das barras
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}'.replace(',', '.'), 
             ha='center', va='bottom', fontsize=10)

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}'.replace(',', '.'), 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()  # Ajusta o layout
plt.show()


top_10 = df.nlargest(10, 'Frota Ativa')
# Criando o gráfico
plt.figure(figsize=(12, 6))
x = np.arange(len(top_10['Município']))  # A posição das barras

# Plotando as barras da população
bars1 = plt.bar(x, top_10['Frota Ativa'], label='Frota Ativa', color='skyblue', alpha=0.7)

# Plotando as barras de acidentes sobrepostas
bars2 = plt.bar(x, top_10['Acidentes'], label='Acidentes', color='orange', alpha=0.7)

# Adicionando título e rótulos
plt.title('Comparativo das 10 Maiores Frotas Ativas e Número de Acidentes nas Cidades')
plt.xlabel('Município')
plt.ylabel('Quantidade')
plt.xticks(x, top_10['Município'], rotation=45)  # Rotaciona os rótulos do eixo x
plt.legend()

# Adicionando os números acima das barras
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}'.replace(',', '.'), 
             ha='center', va='bottom', fontsize=10)

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval):,}'.replace(',', '.'), 
             ha='center', va='bottom', fontsize=10)

plt.tight_layout()  # Ajusta o layout
plt.show()


# df.plot.scatter('População','Frota Total')
# plt.title("População X Frota Total ")
# plt.show()

# df.plot.scatter('População','Frota Ativa')
# plt.title("População X Frota Ativa")
# plt.show()


# df.plot.scatter('População','Acidentes')
# plt.title("População X Acidentes")
# plt.show()

# df.plot.scatter('Frota Ativa','Acidentes')
# plt.title("Frota Ativa X Acidentes")
# plt.show()

# df.plot.scatter('Acidentes','Óbitos')
# plt.title("Acidentes X Óbitos")
# plt.show()


# df.plot.scatter('Acidentes','Feridos e Ilesos','Óbitos')
# plt.title("Acidentes X Feridos e Ilesos")
# plt.show()