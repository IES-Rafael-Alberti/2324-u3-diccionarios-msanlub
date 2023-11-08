'''Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.'''

def ingresarEnDiccionario(diccionario:dict,palabra:str) ->dict:
    '''Añade la palabra en el diccionario
    
    Args:
        diccionario(dict): diccionario vacío al que se le añaden las palabras ingresadas por el usuario.

        palabra(str): palabra (key) con su traducción(value) introducida por el usuario.
        
    Returns:
        devuelve el diccionario con la palabra y su traducción añadid.'''
    palabras = palabra.split(":")
    if len(palabras) == 2:
        diccionario[palabras[0]] = palabras[1]
        return diccionario
    else:
        raise IndexError("Debe ingresar dos palabras separadas por : ")
    
def traducir(frase:str,diccionario:dict) ->str:
    '''traduce la frase que introduzca el usuario según el diccionario antes guardado.
    
    Args:
        frase(str): frase a traducir introducida por el usuario
        diccionario(dict): diccionario con palabras traducidas
        
    Returns:
        devuelve la frase traducida.'''
    
    fraseTraducida = ""
    palabras = frase.split(" ")
    for palabra in palabras:
        if palabra in diccionario:
            fraseTraducida += diccionario[palabra] + " "
        else:
            fraseTraducida += palabra + " "
    return fraseTraducida


def main():
    '''programa principal'''
    #entrada
    diccionario = {}
    palabra = ""
    while palabra != "fin":
        palabra = input("Escribe una palabra y su traducción según el formato (palabra:traducción)(para salir pon fin): ")
        #proceso
        if palabra != "fin":
            ingresarEnDiccionario(diccionario,palabra)
    #salida
    frase = input("Escribe la frase a traducir: ")
    print(traducir(frase,diccionario))
    

if __name__=="__main__":
    main()