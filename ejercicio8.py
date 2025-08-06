lista = []
def cargarcontenido(dato):
    lista.append(dato)

def imprimirlista():
    print(lista)    

def quitarDeLista(dato):
    lista.remove(dato) 

if __name__ == "_main_":
    cargarcontenido("Moises")
    cargarcontenido("Avalos")
    imprimirlista()
    quitarDeLista()
    quitarDeLista("Moises")
    imprimirlista()