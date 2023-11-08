'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''

def nombreCorrecto(persona:dict,nombre:str) ->dict:
    '''Comprueba que el nombre sea str
    
    Args:
        nombre(str):nombre ingresado por usuario
        persona(dict):diccionario donde almacenamos los datos del usuario
        
    Returns:
        devuelve el diccionario con el nuevo parametro.'''
    try:
        if nombre.isalpha():
            persona.setdefault("nombre",nombre)
            return persona
    except AttributeError:
        return AttributeError("El dato no es correcto.Debe ser una palabra.")

def edadCorrecta(persona:dict,edad:str) ->dict:
    '''Comprueba que la edad sea digitos
    
    Args:
        persona(dict):diccionario donde almacenamos los datos del usuario
        edad(int):edad ingresada por el usuario
        
    Returns:
        devuelve el diccionario con el nuevo parametro.'''
    try:
        if int(edad) < 120 and edad.isdigit():
            persona.setdefault("edad",edad)
            return persona
    except ValueError:
        return ValueError("El dato no es correcto.")

def sexoCorrecto(persona:dict,sexo:str) ->dict:
    '''comprueba que el sexo sea um string((
    
    Args:
        persona(dict):diccionario donde almacenamos los datos del usuario
        sexo(str): sexo ingresado por el usuario
    Returns:
        devuelve el diccionario con el nuevo parametro.'''
    if sexo.isalpha():
        persona.setdefault("sexo",sexo)
        return persona

    
def telefonoCorrecto(persona:dict,telefono:int) ->dict:
    '''comprobamos que el telefono sea numeros y con el tamaño correcto
    
    Args:
        persona(dict):diccionario donde almacenamos los datos del usuario
        telefono(int):numeros introducidos por el usuario
    Returns:
        devuelve el diccionario con el nuevo parametro.'''
    if telefono.isdigit() and len(telefono) == 9:
        persona.setdefault("telefono",telefono)
        return persona


def correoIngreso(persona:dict,correo:str) ->dict:
    '''Ingresa el correo del usuario en el diccionario.
    
    Args:   
        persona(dict):diccionario donde almacenamos los datos del usuario
        correo(str):caracteres ingresados por el usuario
        
    Returns:
        devuelve el diccionario con el nuevo parametro.'''

    if correo == "":
        return None
    else:    
        persona.setdefault("correo",correo)
        return persona
    

def main():
    '''programa principal'''
    persona = {}
    nombre = input("Escriba su nombre: ")
    if nombreCorrecto(persona,nombre) == None:
        print("El dato no es correcto,debe ser una cadena de letras.")
    else:
        print(nombreCorrecto(persona,nombre))
    edad = (input("Indique su edad: "))
    print(edadCorrecta(persona,edad))
    sexo = input("Indique su sexo: ")
    if sexoCorrecto(persona,sexo) == None:
        print("El dato no es correcto,deben ser dígitos.")
    else:
        print(sexoCorrecto(persona,sexo))
    telefono = (input("Escriba su teléfono: "))
    if telefonoCorrecto(persona,telefono) == None:
        print("El dato no es correcto, debe tener 6 caracteres.")
    else:
        print(telefonoCorrecto(persona,telefono))
    correo = input("Escriba su correo electrónico: ")
    if correoIngreso(persona,correo) == None:
        print("El dato no es correcto, debe ingresar algún dato.")
    else:
        print(correoIngreso(persona,correo))


if __name__=="__main__":
    main()
