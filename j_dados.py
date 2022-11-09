import random
from operator import itemgetter
import sys
print('='*40)
print('{:^40}'.format('Simulação do lançamento de dados'))
print('='*40)
def iniciaLista(n):
    return [i for i in range(1,n+1)]
def help():
    print("\nMENU")
    print("t - JOGAR;")
    print("x - SAIR;")
    print("w - MOSTRAR ESTATISTICA DO JOGO")
print("Para ver o MENU inteiro prima: h ")
numeros= iniciaLista(6)
global tnumeros 
tnumeros = [0] * 6
numJogo=0
ganhou=0
perdeu=0
Jackpot=0
while True:
  
    command = input("Escolha opção: ")
    if command == 'x':
        sys.exit()
    if command == 'h':
        help()
    if command == 'w':
     
     print('='*40)
     print('{:^40}'.format("Estatistica do JOGO:"))
     print('='*40)
     print(f"Voce jogou:  {numJogo} vezes")
     print(f"Voce ganhou: {ganhou}  vezes")
     print(f"Voce perdeu: {perdeu}  vezes")
     print(f"JACKPOT saiu: {Jackpot}  vezes\n")
     print("Estatistica dos numeros: \n")
     x=0
     for i,n in sorted(list(zip(numeros,tnumeros)), key=itemgetter(1), reverse=True):
      if n>0:
        if x != n:
            if( x != 0 ):
                print()
            x=n
            print(n,' Vezes saiu numero:', end=" ")
        print( i, end=",")
        print()

    elif command == 't':
      
         point_list = [random.choice(range(1, 7)) for i in range(3)]
         print(point_list)
         for j in point_list:
            tnumeros[j-1] += 1 
         numJogo +=1   
        
         Sumdados = sum(point_list)
         msg = f"Soma dos numeros - {sum(point_list)} e menor do que 10! Voce perdeu!" if 3 <= sum(point_list) <= 10 else f"Soma dos numeros - {sum(point_list)} e maior do que 10! Parabens Voce ganhou!"
         if sum(point_list)>10:
           ganhou +=1 
         else:
             perdeu +=1
         print(msg)
         def all_the_same(elements):
           if len(elements) < 1:
             return True
           return len(elements) == elements.count(elements[0])
         if all_the_same(point_list)==True:
           print("OS TRES NUMEROS SAO IGUAIS! PARABENS VOCE GANHOU JACKPOT")
         else:
             print("Os 3 numeros são diferentes, Lamentamos voce não ganhou JACKPOT")
         if all_the_same(point_list)==True:
          Jackpot +=1    
    
    
  
