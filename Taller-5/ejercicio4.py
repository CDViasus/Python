n = int(input("Ingrese la cantidad de valores a promediar\n")) #n valores
suma=0
i=1
while(i<=n):
    print("Ingrese el valor N°", i)
    valores = float(input())
    suma=suma+valores
    i+=1
prom = suma/valores
print("El promedio de los valores es:", prom)