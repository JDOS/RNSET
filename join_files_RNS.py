import os
import pandas as pd
import csv

erros=[]
for i in range(0,5298):
	if not os.path.exists("files/"+str(i)+".xlsx"):
		erros.append(i)

print(f"Arquivos faltantes: {erros}")


def populacao_0(list_todos):
	list_populacao_0 =[]
	for index,i in enumerate(list_todos):
		if(i[1]==0):
			print(index,i[0],i[1])
			list_populacao_0.append(index)

	print(f"Cidades com arquivos zerados: {list_populacao_0}")

def zerar_linha_populacao_0(list_todos):
	for i in list_todos:
		if(i[1]==0):
			i[1] = 0
			i[2] = 0
			i[3] = 0
			i[4] = 0
			i[5] = 0
			i[6] = 0
			i[7] = 0

	return list_todos

def ler_csv_cidades():
	cidades=[]
	with open('cidades.csv', mode='r') as arquivo_csv:
	    leitor = csv.reader(arquivo_csv, delimiter=';')  # Se o separador for ';'
	    
	    # Iterar sobre as linhas
	    for linha in leitor:
	        print(linha)
	        cidades.append(linha)

	return cidades




def criar_csv():
	cidades = ler_csv_cidades()


	list_todos=[]
	for index,i in enumerate(range(0,5300)):
		if os.path.exists("files/"+str(i)+".xlsx"):
			# Ler o arquivo Excel
			df = pd.read_excel("files/"+str(i)+".xlsx")
			linha_especifica = df.iloc[0] 
			linha = linha_especifica.tolist()
			#print(linha)
			linha.insert(0, cidades[index][0])
			list_todos.append(linha)

	populacao_0(list_todos)

	list_todos = zerar_linha_populacao_0(list_todos)

	# for i in list_todos:
	# 	print(i)
	#cabeçalho
	cabecalho=['Município','População','Frota Total','Frota Ativa','Acidentes','Veículos Envolvidos','Feridos e Ilesos','Óbitos']
	list_todos.insert(0, cabecalho)

	with open('join_RNS.csv', mode='w', newline='\n') as arquivo_csv:
	    writer = csv.writer(arquivo_csv, delimiter=';')
	    for i in list_todos:
	    	writer.writerow(i)


ler_csv_cidades()
criar_csv()