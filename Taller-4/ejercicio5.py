num1 = int(input("ingrese primer numero\n"))
num2 = int(input("ingrese segundo numero\n"))
if (num1<=33 and num1>0):
    if(num2<=33 and num2>0):
        bit_a_bit = {
        "and": num1 & num2, 
        "or": num1 | num2,
        "not": [~num1,~num2],
        "xor": num1 ^ num2,
        "right_shift": [num1>>2,num2>>2],
        "left_shift": [num1<<5,num2<<5],
        }
        print("Operadores Bitwise", bit_a_bit)
else:
    print("El numero no esta dentro del rango de 0 a 33")