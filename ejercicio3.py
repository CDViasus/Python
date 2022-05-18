n1 = 9 #dia
n2 = 8 #mes
if(n1 != n2):
 print(n1 , " & " , n2 , "son diferentes")
 if (n1 > n2):
  print(n1 , "es mayor a" , n2)
  if(n2 <= n1):
   print(n2 , "es menor o igual que" , n1)
 elif (n1 < n2):
  print(n1 , "es menor a" , n2)
  if (n2 >= n1):
   print(n2 , "es mayor o igual que" , n1)
 elif(n1 == n2):
  print(n1 , " & " , n2 , "son iguales")
else:
 print("Los valores no son validos")