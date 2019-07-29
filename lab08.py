#Manuela Rafael Onofre de Sousa - RA:202534

N=int(input()) #input do número de evoluções
aux=1 #só pra setar quantas vezes acrescentaremos informações no banco de dados
bancodedados=[] #será uma matriz preenchida pelos valores que formarão o banco de dados
identificador=[] #será um vetor que conterá os identificadores dos pokémons
n=-1
while (aux<=N):
    linha=input()
    dados=[int(a) for a in linha.split()] #dá split nos valores que recebemos em linha e guarda em diferentes posições de uma lista
    M= float(dados[2]/dados[1])
    if not dados[0] in identificador: #se o primeiro número de dados não estiver em identificador
        n=n+1
        identificador.append(dados[0]) #coloca o número no identificador
        bancodedados.append([]) #cria uma nova linha na matriz do banco de dados
        bancodedados[n].append(M) #coloca o valor de M na nova linha n
        print(bancodedados)
    else:
        bancodedados[n].append(M) #coloca o valor de M na linha n existente
        print(bancodedados)
    aux=aux+1
while True:
    entrada=input()
    vet=[int(b) for b in entrada.split()] #da slip no I e PCa que estão sendo consultados na entrada
    I=vet[0]
    PCa=vet[1]
    if I!=0 or PCa!=0: #enquanto os valores recebidos em entrada não forem 0 0 o programa executa
        if I==identificador[n]:
            Mm = sum(bancodedados[n]) // len(bancodedados[n])
            PCf=Mm*PCa
            print(PCf)

    else:
        break
