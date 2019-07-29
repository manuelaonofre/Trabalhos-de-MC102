#Manuela Rafael Onofre de Sousa - RA:202534
#O programa tem como objetivo a criação de uma matriz ixj(que corresponde a NxN, dado o input N) em que, dado um item[i][j], quando i for divisor de j ou vice-versa esse item seja um '*' e quando i não for divisor de j nem vice-versa o item seja um '-'
N=int(input()) #a dimensão da matriz é NxN
matriz=[['-' for j in range(N)] for i in range(N)] #cria uma matriz de tamanho NxN preenchida por '-'
asteriscos=0 #o número de asteriscos ainda é 0
for i in range(N): #para linhas até a N-ésima linha
    for j in range(N): #para colunas até a N-ésima coluna
        if (i+1)%(j+1)==0 or (j+1)%(i+1)==0: #se i for divisor de j ou vice versa
            matriz[i][j]= '*' #substitui o item dessa posição por um '*'
            asteriscos=asteriscos+1 #contabiliza que foi acrescentado um asterisco

for i in range(N): #percorre as linhas da matriz
    for j in range(N): #percorre as colunas da matriz
        print(matriz[i][j], end='') #printa a posição até que seja encontrado um espaço
    print() #printa um espaço para que seja criada a próxima linha
print(asteriscos) #printa o número de asteriscos que a matriz contem
