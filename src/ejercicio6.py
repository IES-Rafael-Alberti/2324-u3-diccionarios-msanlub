'''Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''

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
    
    persona.keys(nombre)
    print(persona)
    persona.keys(edad)
    print(persona)
    persona.keys(sexo)
    print(persona)
    persona.keys(telefono)
    print(persona)
    persona.keys(correo)
    print(persona)

def main():
    #entrada
    persona = {}
    nombre = input("Escriba su nombre: ")
    edad = input("Indique su edad: ")
    sexo = input("Indique su sexo: ")
    telefono = input("Escriba su teléfono: ")
    correo = input("Escriba su correo electrónico: ")
    #proceso y salida
    ingreso = ingresarPersona(persona,nombre,edad,sexo,telefono,correo)

if __name__=="__main__":
    main()
