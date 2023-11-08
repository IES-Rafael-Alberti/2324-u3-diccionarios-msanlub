'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''

def nombreCorrecto(nombre:str) ->bool:
    '''Comprueba que el nombre sea str
    
    Args:
        nombre(str):nombre ingresado por usuario
        
    Returns:
        si es correcto devuelve True y sino False.'''
    if nombre.isalpha():
        return True
    else:
        return False
    
def edadCorrecta(edad:int) ->bool:
    '''Comprueba que la edad sea digitos
    
    Args:
        edad(int):edad ingresada por el usuario
        
    Returns:
        si la edad es correcta devuelve True y si no False.'''
    if edad < 120 and edad.isdigit():
        return True
    else:
        return False

def sexoCorrecto(sexo:str) ->bool:
    '''comprueba que el sexo sea um string((
    
    Args:
        sexo(str): sexo ingresado por el usuario
    Returns:
        si el sexo introducido es un string devuelve True y si no False'''
    if sexo.isalpha():
        return True
    else:
        return False
    
def telefonoCorrecto(telefono:int) ->bool:
    '''comprobamos que el telefono sea numeros y con el tamaño correcto
    
    Args:
        telefono(int):numeros introducidos por el usuario
    Returns:
        si el telefono esta con el formato correcto(número y tamaño) devuelve True, sino devuelve False'''
    if telefono.isdigit() and len(telefono) < 9:
        return True
    else:
        return False
    
def correoCorrecto(correo:str) ->bool:
    '''comprobamos que el correo sea alfanumerico.
    
    Args:   
        correo(str):caracteres ingresados por el usuario
        
    Returns:
        si el correo es de formato correcto devuelve True,sino devuelve False.'''
    if correo.isalnum():
        return True
    else:
        return False
    
def ingresarPersona(persona:dict,nombre:str,edad:str,sexo:str,telefono:str,correo:str) ->dict:
    '''Devuelve el diccionario con los datos ingresados del usuario.
    
    Args:
        persona(dict): diccionario vacío donde se van ingresando los datos de la persona
        nombre(str): input del nombre del usuario
        edad(str):input de la edad del usuario
        sexo(str):input del sexo del usuario
        telefono(str):input del número de teléfono del usuario
        correo(str):input del correo electrónico del usuario
    Returns:
        devuelve el diccionario con los datos del usuario.Imprime cada resultado que se ingresa nuevo.
    '''
    
    persona.setdefault(nombre)
    persona.setdefault(edad)
    persona.setdefault(sexo)
    persona.setdefault(telefono)
    persona.setdefault(correo)
    for parametro in persona:
        print(parametro)
    


def main():
    '''programa principal'''
    #entrada
    persona = {}
    nombre = input("Escriba su nombre: ")
    edad = int(input("Indique su edad: "))
    sexo = input("Indique su sexo: ")
    telefono = int(input("Escriba su teléfono: "))
    correo = input("Escriba su correo electrónico: ")
    #proceso y salida
    ingreso = ingresarPersona(persona,nombre,edad,sexo,telefono,correo)

if __name__=="__main__":
    main()
