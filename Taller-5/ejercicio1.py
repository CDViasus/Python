n1 = int(input("Ingrese un numero par\n"))
if(n1%2 == 0):
 n2 = 0
 while(n1 != n2):
      n2 = int(input("Ingrese el numero nuevamente\n"))
      if(n1 == n2):
           break
      elif(n2%2>0):
           break
      else:
       n2 = int(input("Ingrese el numero nuevamente\n"))   
else:
 print("el numero no es par")