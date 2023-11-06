'''Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''

def dameSimboloDivisa(divisas:dict,codigoDeDivisa:str) -> str:
    '''Devuelve el simbolo de una divisa 
    Args:
        divisas (dict): Diccionario con pares (codigoDivisa:simboloDivisa)
        codidoDeDivisa (str): el codigoDivisa a buscar

    Returns:
        str: el simbolo de la divisa que corresponde al codigoDeDivisa. Si codigoDeDivisa no existe, devuelve "".
    '''

    return divisas.get(codigoDeDivisa,"")

if __name__=="__main__":
    #entrada
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    codigoDeDivisa = input("Indica la divisa a elegir: ")

    #proceso
    simboloDivisa = dameSimboloDivisa(divisas,codigoDeDivisa)

    #salida
    print("Su símbolo es: " + simboloDivisa)