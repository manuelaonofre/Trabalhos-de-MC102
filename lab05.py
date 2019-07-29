ken=50
ryu=50
placar=0
combo=0
rodada=0
golpe=0

for rodada in range(0,2):
	ken=50
	ryu=50
	combo=0	
	
	while True:
		golpe=int(input())
		if golpe>0 and combo>0 and ken<=combo+golpe:
			print("Ken: " +str(ken)+ " - " +str(combo+golpe)+ " = " +str(ken-combo-golpe))
			ken=ken-combo-golpe			
			break
		elif golpe<0 and combo<0 and ryu<=-(combo+golpe):
			print("Ryu: " +str(ryu)+ " - " +str(-combo-golpe)+ " = " +str(ryu+combo+golpe))
			ryu=ryu+combo+golpe
			break
		if golpe>0 and combo>=0:
			combo=combo+golpe
		elif golpe<0 and combo<=0:
			combo=combo+golpe
		elif golpe>0 and combo<0:
			print("Ryu: " +str(ryu)+ " - " +str(-combo)+ " = " +str(ryu+combo))
			ryu=ryu+combo
			combo=golpe
			if ken<=golpe:
				print("Ken: " +str(ken)+ " - " +str(golpe)+ " = " +str(ken-golpe))
				ken=ken-golpe
				break
		elif golpe<0 and combo>0:
			print("Ken: " +str(ken)+ " - " +str(combo)+ " = " +str(ken-combo))
			ken=ken-combo
			combo=golpe
			if ryu<=-golpe:
				print("Ryu: " +str(ryu)+ " - " +str(-golpe)+ " = " +str(ryu+golpe))
				ryu=ryu+golpe
				break
	
	if rodada == 0 and ken<=0:
		placar=1 #placar=1 significa que o ryu ganhou essa partida
	elif rodada == 0 and ryu<=0:
		placar=-1 #placar=-1 significa que o ken ganhou essa partida
	elif rodada == 1 and placar==1 and ken<=0:
		print("Ryu venceu")
	elif rodada == 1 and placar==-1 and ken<=0:
		print("empatou")
	elif rodada == 1 and placar==1 and ryu<=0:
		print("empatou")
	elif rodada == 1 and placar==-1 and ryu<=0:
		print("Ken venceu")






		

