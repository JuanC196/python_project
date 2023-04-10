def registro():

  global diccionario

  diccionario={}
  continua ="s"
  while continua=="s":
        user=input("Ingrese un usuario:")
        password=input("Ingrese una contraseña:")
        diccionario[user]=password
        continua=input("Quiere Registrar otro Usuario? [s/n]")
  return diccionario

registro()

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for user in diccionario:
        print(user,diccionario[user])
imprimir(diccionario)

def login(diccionario):
  
  while True:
    user=input("Ingresa tu Usuario:")
    password=input("Ingresa tu contraseña: ")

    if user not in diccionario:
      print("Usuario no Encontrado, Vuelve a intentarlo") 
      break

    if diccionario[user] == password:
        print("Ingreso Exitoso!! bienvenido " + user)
        break 

    else:
        print("Ingreso fallido algun dato no coincide, Intenta de Nuevo ")
login(diccionario) 