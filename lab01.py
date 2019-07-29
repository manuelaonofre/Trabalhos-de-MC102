#Manuela Rafael Onofre de Sousa - 202534
#O programa tem como objetivo calcular a circunferência de um planeta com base da observação do ângulo A entre duas localidades e da distância D entre elas

#Scan das entradas
D = float(input())
A = float(input())

#Cálculo da circunferência
C = 360 * D / A

#Transformando o valor da circunferência de estádios para kilômetros
Ce = C
Ckm = C * 0.1764

#Imprimindo as saídas
print("%.1f" %Ce)
print("%.1f" %Ckm)
