#Manuela Rafael Onofre de Sousa - RA.: 202534
#O objetivo do programa é simular o estado de uma população após um número de dias obedecendo às regras de interação humano/zumbi

mxn = input() #input do número de linhas e colunas da matriz que representa a população
mxn = mxn.split()
m = int(mxn[0])
n = int(mxn[1])

mat = [] #matriz vazia que após a inserção dos valores será a matriz lida
auxmat = [] #matriz auxiliar que será printada e sofrerá as operações
dias = int(input()) #número de dias a serem analizados

#0 representa o vazio, 1 um humano e 2 um zumbi

for i in range (m): #para cada linha de 0 até m-1
	linha = input() #input de casa uma das m linhas da matriz
	linha = linha.split() #transforma o input numa lista com n itens
	linha2 = linha[:]
	mat.append(linha) #insere a linha dentro da matriz vazia
	auxmat.append(linha2)

print("iteracao 0")
for i in range(m): #printa a matriz inicial do estado da população item por item
	for j in range (n):
		print(mat[i][j], end="") #printa elemento por elemento da linha, quando percorrer todos os j
	print()	#printa nada (pula linha) e vai pro próximo m

#insere uma moldura de zeros que serve para auxiliar nas operações com os elementos das pontas das matrizes
mat.insert(0, ["0" for x in range(n)])
auxmat.insert(0, ["0" for x in range(n)])
mat.append(["0" for x in range(n)])
auxmat.append(["0" for x in range(n)])

for i in range(m+2):
	mat[i].insert(0, "0")
	mat[i].insert(n+1, "0")
	auxmat[i].insert(0, "0")
	auxmat[i].insert(n+1, "0")


iteracao = 0
for d in range (dias): #para um número de dias
	iteracao = iteracao+1
	print ("iteracao",iteracao)
	for i in range (1,m+1): #percorre os elementos da matriz que não fazem parte da moldura de zeros
		for j in range (1,n+1):
			naocome = 0 #elementos que zumbis não podem comer
			lutadores = 0 #contador de humanos que podem matar zumbis
			procriadores = 0 #contador de humanos que podem procriar
			for k in [i-1,i,i+1]:
				for l in [j-1,j,j+1]:
					if mat[i][j] == "1": #caso o elemento x da matriz seja um humano
						if mat[k][l] == "2": #caso algum elemento vizinho seja um zumbi
							auxmat[i][j]= "2"
							continue
					elif mat[i][j] == "2": #caso o elemento x da matriz seja um zumbi
						if (mat[k][l] == "0" or mat[k][l] == "2"):#caso algum elemento vizinho seja vazio ou outro zumbi
							naocome = naocome+1 #atualiza valor de elementos que zumbis nao podem comer
							if naocome==9: #se todos os elementos vizinhos foram incomiveis
								auxmat[i][j]="0" #zumbi morre de fome
								continue
						if mat[k][l] == "1": #caso algum elemento vizinho seja um humano
							lutadores = lutadores+1
							if lutadores==2: #se pelo menos dois vizinhos forem humanos
								auxmat[i][j]="0" #zumbi morre
								continue
					elif mat[i][j] == "0": #caso o elemento x da matriz seja um zumbi
						if mat[k][l] == "1": #se algum elemento vizinho for humano
							procriadores=procriadores+1
							if procriadores==2: #se existirem exatamento dois humanos
								auxmat[i][j]="1" #o elemento x vira um humano
							else if procriadores>2: #se existirem mais de dois humanos
								auxmat[i][j]="0" #o elemento não vira um humano



	for i in range(1,m+1): #printa a matriz sem a moldura elemento por elemento
		for j in range (1,n+1):
			print(auxmat[i][j], end="") #printa elemento por elemento da linha, quando percorrer todos os j
		print()	#printa nada (pula linha) e vai pro próximo m

	for i in range(m+1): #atualiza os valores da mat com os valores da auxmat sem estabelecer uma ligação entre eles
		mat[i]=auxmat[i][:]
