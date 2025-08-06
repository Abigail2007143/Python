numero = 100000000 
while True:
    bandera = 0
    for x in range(2, int(numero/2)):
        if(numero % x == 0):
            esPrimo = False
            break

    if esPrimo :
        print(f"Es primo: {numero}")  

    numero = numero + 1      