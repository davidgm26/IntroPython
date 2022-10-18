from operator import indexOf

numElegido = int (input("Introduzca el numero del que quiere imprimir la tabla de multiplicar"))
for num in range(0,11):
    print ("%d * %d = %d"%(numElegido,num, num*numElegido)) 
    
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for num in range(1,6):
    for numMultiplicado in range (0,11):
        print("%d * %d = %d"%(num,numMultiplicado, numMultiplicado*num))