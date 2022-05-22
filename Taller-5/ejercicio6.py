import random
num = int(input("Ingrese un numero de 1 a 10\n")) 
rifa = random.randint(1, 10) 
if (num>0 and num<=10):    
 if(num != rifa):
  print("Perdiste")
 else:
  print("Ganaste")
else:
    print("Numero no valido")