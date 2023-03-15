


class Validacion():
    
    
    @staticmethod
    def nif(nif: str):
        letras_nif = 'TRWAGMYFPDXBNJZSQVHLCKE'
        nif = nif.upper()
        if not nif[0:-1].isnumeric():
            return False
            
        dni = int(nif[0:-1])
        
        posLetra = dni % 23
        
        return letras_nif[posLetra] == nif[-1]
    
    
    @staticmethod            
    def edad(edad):
        return int(edad) >= 0 and int(edad) < 130
    
    @staticmethod
    def telefono(telefono: str):
        return telefono.isnumeric() and int(telefono[0]) in (6,7,8,9)
    
    @staticmethod
    def email(correo):
        posArroba = 0
        emailValido = False
        
        if not emailValido:
            if correo.find("@") > 0:
                posArroba = correo.find("@")
                if correo.find(".", posArroba, -1) < (len(correo) -1) and correo.find(".", posArroba, -1) > posArroba and 1 < correo.find(".", posArroba, -1) - posArroba:
                    emailValido = True
        
        return emailValido