'''Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''

def guardarDatosEnDiccionario(nombre:str,edad:str,direccion:str,telefono:str) ->dict:
    '''Devuelve un diccionario con los datos ingresados por el usuario. 
    Args:
        nombre(str),edad(str),telefono(str),dirección(str): datos ingresados por el usuario

    Returns:
        dict: diccionario actualizado con los datos.
    '''

    datos = {'nombre':nombre,'edad':edad,'direccion':direccion,'telefono':telefono}
    return datos

def main():
    #entrada
    nombre = input("Escriba su nombre: ")
    edad = input("Indique su edad: ")
    direccion = input("Diganos su dirección: ")
    telefono = input("Por último indique su teléfono de contacto: ")
    #proceso:
    datosDict = guardarDatosEnDiccionario(nombre,edad,direccion,telefono)
    #salida
    print(datosDict['nombre'] + " tiene " + datosDict['edad'] + " años, vive en " + datosDict['direccion'] + " y su número de teléfono es " + datosDict['telefono'])

if __name__=="__main__":
    main()