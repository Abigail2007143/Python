texto = input('introduce un titulo')
nombre_fichero = 'archivo-' + texto + '.txt'
f = open(nombre_fichero, 'w') #apertura w= write, r = reaad, a = append
mensaje = input("Ingrese un mentaje: ")
f.write(f'{mensaje}\n')
f.close()

