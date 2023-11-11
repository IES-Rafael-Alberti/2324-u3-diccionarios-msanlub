'''Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato'''


def ingresoEnLista(listaCompra:dict,articulo:str,precio:float) ->dict:
    '''Añade en la lista de la compra los articulos y los precios ingresados por el usuario.
    
    Args:
        listaCompra(dict): diccionario vacío
        articulo(str): articulo ingresado por el usuario
        precio(str): precio del articulo ingresado por el usuario
    
    Return:
        devuelve el diccionario con los articulos como keys y los precios como valores.'''
    listaCompra.setdefault(articulo,precio)
    return listaCompra

def precioTotal(listaCompra:dict,precio:float) ->float:
    '''Calcula el precio total de todos los artículos
    
    Args:
        listaCompra(dict): diccionario vacío
        precio(str): precio por artículo ingresado por el usuario
        
    Returns:
        devuelve el precio total de todos los articulos.'''
    total = 0
    for precio in listaCompra.values():
        total += precio
    return total
    

def main():
    #entrada
    listaCompra = {}
    articulo = ""
    precio = 1
    while articulo != "fin" and precio != 0:
        articulo = input("Escribe el artículo: ")
        precio = float(input("Indica el precio del artículo: "))
        #proceso
        if articulo != "fin" and precio != 0:
            lista = ingresoEnLista(listaCompra,articulo,precio)
            totalPrecio = precioTotal(listaCompra,precio)
    #salida
    print("\nLista de la compra \n")
    for articulo,precio in lista.items():
        print(str(articulo) + "\t" + str(precio) + "\n")
    print("El precio total es :" + str(totalPrecio))
        


if __name__=="__main__":
    main()
