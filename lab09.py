#Manuela Rafael Onofre de Sousa - RA.:202534
#O objetivo do programa é avaliar os valores diários dos blocos de ações de quatro empresas durante um certo período de dias e decidir qual é o melhor dia para comprar e vender as ações de cada empresa, sendo que as ações de cada empresa só podem ser compradas no máximo uma vez, para comprar ações de uma empresa deve-se vender as ações previamente compradas de outra empresa e pode-se vender as ações de uma empresa e comprar a de outra no mesmo dia.
dias=int(input()) #Quantidade de dias no período analisado
empresa1=[] #Lista que conterá os valores das ações da empresa 1 para os dias analisados
i=0
while (i<dias): #Enquanto i for menor que o número de dias
    empresa1.append(float(input())) #Acrescenta um dado (valor da ação) na lista da empresa
    i=i+1
empresa2=[]
j=0
while (j<dias): #Enquanto j for menor que o número de dias
    empresa2.append(float(input())) #Acrescenta um dado (valor da ação) na lista da empresa
    j=j+1
empresa3=[]
k=0
while (k<dias): #Enquanto k for menor que o número de dias
    empresa3.append(float(input())) #Acrescenta um dado (valor da ação) na lista da empresa
    k=k+1
empresa4=[]
l=0
while (l<dias): #Enquanto l for menor que o número de dias
    empresa4.append(float(input())) #Acrescenta um dado (valor da ação) na lista da empresa
    l=l+1
#Definir as variáveis de dias de compra (c1,c2,c3 e c4) e dias de venda (v1,v2,v3 e v4) e a variável que guardará o maior valor de lucro (maior)        
c1=0
c2=0
c3=0
c4=0
v1=0
v2=0
v3=0
v4=0
maior=0
#Analisa os dias de compra e venda, sendo a posição dos dias de venda maiores ou iguais aos dias de compra de ações numa empresa
for c1 in range(0,dias): #para dia de compra da empresa 1 no intervalo do primeiro ao último dia do input
	for v1 in range(c1,dias): #para dia de venda da empresa 1 no intervalo do dia de compra 1 ao último dia do input
		for c2 in range(0,dias): #para dia de compra da empresa 2 no intervalo do primeiro ao último dia do input
			for v2 in range(c2,dias): #para dia de venda da empresa 2 no intervalo do dia de compra 2 ao último dia do input
				for c3 in range(0,dias): #para dia de compra da empresa 3 no intervalo do primeiro ao último dia do input
					for v3 in range(c3,dias): #para dia de venda da empresa 3 no intervalo do dia de compra 3 ao último dia do input
						for c4 in range(0,dias): #para dia de compra da empresa 4 no intervalo do primeiro ao último dia do input
							for v4 in range(c4,dias): #para dia de venda da empresa 4 no intervalo do dia de compra 4 ao último dia do
								#condições para que os dias de compra e venda sejam possíveis
								if (c1>=v2 or v1<=c2) and (c1>=v3 or v1<=c3) and (c1>=v4 or v1<=c4):
									if (c2>=v3 or v2<=c3) and (c2>=v4 or v2<=c4):
										if (c3>=v4 or v3<=c4):
											lucro1 = empresa1[v1]-empresa1[c1] #cálculo de lucro das empresas
											lucro2 = empresa2[v2]-empresa2[c2]
											lucro3 = empresa3[v3]-empresa3[c3]
											lucro4 = empresa4[v4]-empresa4[c4]
											lucro = lucro1+lucro2+lucro3+lucro4 #cálculo do lucro total
											if lucro>=maior: #definição do maior lucro total possível
												c1max=c1
												c2max=c2
												c3max=c3
												c4max=c4
												v1max=v1
												v2max=v2
												v3max=v3
												v4max=v4
												maior=lucro
												maior1=lucro1
												maior2=lucro2
												maior3=lucro3
												maior4=lucro4
#definição para os prints das saídas (lucro maior que 0) e print do lucro total das operações
if maior1>0:
	print("acao 1: compra %d, venda %d, lucro %.2f" % (c1max+1, v1max+1, maior1))
if maior2>0:
	print("acao 2: compra %d, venda %d, lucro %.2f" % (c2max+1, v2max+1, maior2))
if maior3>0:
	print("acao 3: compra %d, venda %d, lucro %.2f" % (c3max+1, v3max+1, maior3))
if maior4>0:
	print("acao 4: compra %d, venda %d, lucro %.2f" % (c4max+1, v4max+1, maior4))
print("Lucro: %.2f" % (maior))			
