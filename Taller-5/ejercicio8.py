n1 = int(input("Escriba el primer numero\n"))
n2 = int(input("Escriba el segundo numero\n"))
n3 = int(input("Escriba el tercer numero\n"))
print("1. Sumar - 2. Restar - 3. Multiplicar - 4. Dividir")
cont = 0 #Contador
while(cont == 0):
 option = int(input("Escoja la Operacion que desea realizar\n"))
 if option == 1:
  print("La Suma es: ", n1+n2+n3)
  cont+=1
 elif option == 2:
  print("La Resta es: ", n1-n2-n3)
  cont+=1
 elif option == 3:
  print("La Multiplicacion es:", n1*n2*n3)
  cont+=1
 elif option == 4:
  print("La Division es: ", round(n1/n2/n3,2))
  cont+=1