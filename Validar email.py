##  ___________@________.____  ##
## bladimir.peralta@iescesarmanrique.com ##


emailValido = False

while not emailValido:
    correo = input("Introduce tu correo electrónico: ")


    if correo.find("@") > 0:
        posArroba = correo.find("@")
        if correo.find(".") < (len(correo) -1) and correo.find(".") > posArroba and (correo.find('@') - correo.find(".")) > 1:
            emailValido = True


    if not emailValido:
        print(correo + " NO ES un email valido")
    else:
        print(correo + " ES un email valido")