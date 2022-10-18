primo = True
num = int (input("Introduzca un número para comprobar si es primo o no  "))
for cont in range (2, num):
      
    if num % cont == 0: 
        primo = False
if (primo):
    print("Es numero primo") 
else:
    print("No es numero primo")   
       