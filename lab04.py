#Manuela Rafael Onofre de Sousa - 202534
#O programa tem como objetivo auxiliar no gerenciamento de um estacionamento que possui uma certa capacidade, impedindo que veículos que não caibam no estacionamento de entrar e informando da capacidade atual aos que chegam

#Scan da capacidade
C = int(input())

#Scan do valor i do tamanho do carro
i = int(input())
while i != 0:

  
#Condição para estacionamento lotado
  if C < i:
   print("Veiculo muito grande! Capacidade restante: " +str(C))

#Condição para quando há vagas
  elif C >= i: 
   C = C - i

#Condição para quando o carro está entrando   
   if i > 0:
    print("Seja bem-vindo! Capacidade restante: " +str(C))

#Condição para quando o carro está saindo
   else:
    print("Volte sempre! Capacidade restante: " +str(C))

  i = int(input())    




