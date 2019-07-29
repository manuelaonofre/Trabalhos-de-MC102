#Manuela Rafael Onofre de Sousa - RA.: 202534

#Vida inicial de Ken e Ryu
ken=2000
ryu=2000
#Placar=0 significa que ninguém ganhou um jogo ainda. A variável placar indica se há jogos ganhos ou não.
placar=0
#A variável combo guarda os golpes sucessivos de cada personagem
combo=0
#A variável rodada serve para contabilizar duas rodadas e fazer o programa funcionar para duas rodadas de luta entre os personagens, rodada=0 é a primeira rodada
rodada=0
#O golpe é o input que subtrai na vida dos personagens. Seria o dano que um personagem causa no outro. Os golpes positivos são aplicados na vida do Ken e os negativos, na vida do Ryu.
golpe=0

#O programa roda em duas rodadas
for rodada in range(0,2):
	ken=2000
	ryu=2000
	combo=0	

	#Condição de loop que só se encerra quando algum personagem morre
	while True:
		golpe=int(input())
		div1=1
		div2=-1
		acu=0
		if golpe>0:
			while (div1<=golpe-1):
				if(golpe%div1==0):
					acu=acu+div1
				div1=div1+1
		elif golpe<0:
			while (div2>=golpe+1):
				if(golpe%div2==0):
					acu=acu+div2
				div2=div2-1
		if acu==golpe:
                        golpe=golpe*3
		elif acu!=golpe:
			golpe=golpe
			acu=0
			i1=1
			i2=-1
			if golpe>0:
				while (i1<golpe) and acu!=golpe:
					acu=acu+i1
				i1=i1+1
			if golpe<0:
				while(i2>golpe) and acu!=golpe:
					acu=acu+i2
				i2=i2-1

			if acu==golpe:
				golpe*2
			else:
				golpe=golpe

		if golpe>0 and combo>0 and ken<=combo+golpe: #Se o golpe e o combo estiverem sendo aplicados ao Ken e o mesmo morre
			print("Ken: " +str(ken)+ " - " +str(combo+golpe)+ " = " +str(ken-combo-golpe)) #Printa o dano levado por Ken e o seu novo valor de vida
			ken=ken-combo-golpe	#Atualiza a vida do Ken		
			break
		elif golpe<0 and combo<0 and ryu<=-(combo+golpe): #Se o golpe e o combo estiverem sendo aplicados ao Ryu e o mesmo morre
			print("Ryu: " +str(ryu)+ " - " +str(-combo-golpe)+ " = " +str(ryu+combo+golpe)) #Printa o dano levado por Ryu e o seu novo valor de vida
			ryu=ryu+combo+golpe #Atualiza a vida do Ryu
			break
		if golpe>0 and combo>=0: #Se o golpe e o combo ou o golpe com o combo zerado estiverem sendo aplicados ao Ken, mas o mesmo continua vivo
			combo=combo+golpe #Atualiza o valor do combo
		elif golpe<0 and combo<=0: #Se o golpe e o combo ou o golpe com o combo zerado estiverem sendo aplicados ao Ryu mas o mesmo continua vivo
			combo=combo+golpe #Atualiza o valor do combo
		elif golpe>0 and combo<0: #Se o golpe é aplicado ao Ken mas o último combo estava sendo aplicado ao Ryu
			print("Ryu: " +str(ryu)+ " - " +str(-combo)+ " = " +str(ryu+combo)) #Printa a vida do Ryu
			ryu=ryu+combo #Atualiza a vida do Ryu
			combo=golpe #Começa o novo combo que está sendo aplicado ao Ken e é igual ao valor do novo golpe
			if ken<=golpe: #Se o Ken morre com esse golpe aplicado
				print("Ken: " +str(ken)+ " - " +str(golpe)+ " = " +str(ken-golpe)) #Printa o dano levado por Ken e o seu novo valor de vida
				ken=ken-golpe #Atualiza a vida de Ken
				break
		elif golpe<0 and combo>0: #Se o golpe é aplicado ao Ryu mas o último combo estava sendo aplicado ao Ken
			print("Ken: " +str(ken)+ " - " +str(combo)+ " = " +str(ken-combo)) #Printa o dano levado por Ken e o seu novo valor de vida
			ken=ken-combo #Atualiza a vida do Ken
			combo=golpe #Começa ao novo combo que está sendo aplicado ao Ryu e é igual ao valor do novo golpe
			if ryu<=-golpe: #Se o Ryu morre com esse golpe aplicado
				print("Ryu: " +str(ryu)+ " - " +str(-golpe)+ " = " +str(ryu+golpe))#Printa o dano levado por Ryu e o seu novo valor de vida
				ryu=ryu+golpe #Atualiza a vida do Ryu
				break
	
	if rodada == 0 and ken<=0: #Se o Ken tiver morrido e for a primeira rodada
		placar=1 #Atualizar o valor do placar para placar=1 significa que o ryu ganhou essa partida
	elif rodada == 0 and ryu<=0: #Se o Ryu tiver morrido e for a primeira rodada
		placar=-1 #placar=-1 significa que o ken ganhou essa partida
	elif rodada == 1 and placar==1 and ken<=0: #Se o Ken tiver morrido pela segunda vez e for a segunda rodada 
		print("Ryu venceu")
	elif rodada == 1 and placar==-1 and ken<=0: #Se o Ken tiver morrido mas o Ryu tiver morrido na rodada anterior e for a segunda rodada
		print("empatou")
	elif rodada == 1 and placar==1 and ryu<=0: #Se o Ryu tiver morrido mas o Ken tiver morrido na rodada anterior e for a segunda rodada
		print("empatou")
	elif rodada == 1 and placar==-1 and ryu<=0: #Se o Ryu tiver morrido pela segunda vez e for a segunda rodada
		print("Ken venceu")






		

