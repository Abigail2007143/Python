inicio = 0
limite = 0
print("Prog. que imp. los num pares entre dos num dados")
inicio = int(input ("Ingrese el valor de inicio:"))
limite = int(input("Ahora el valor de fin"))
for x in range(inicio,limite): 
    if x % 2 == 0 :
        print(f" / {x} ", end=" ")