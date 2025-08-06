diccUsuarios = {"admin":"12345", "moises":"asdf"}

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

intentos = 0
if user in diccUsuarios:
    #usuario existente
    intentos = intentos + 1
    while intentos < 3:
        if password == diccUsuarios[user]:
            print("Acceso correcto")
            break
        else:
            print("Acceso incorrecto")
            intentos = intentos + 1
            password = input(f"Intentos {intentos} de 3. Reescriba su contraseña: ") 
else:
    print("Usuario no regisrado")                