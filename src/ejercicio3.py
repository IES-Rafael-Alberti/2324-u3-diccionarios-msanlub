'''Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''

def precioTotal(frutas:dict,fruta:str,kilos:float) ->float:
    '''Devuelve el precio de los kilos de la fruta que quiere el usuario.
     
    Args:
        frutas(dict),fruta(str),kilos(float)

    Returns:
        dict: diccionario actualizado con los datos.
    '''
    if fruta in frutas:
        return frutas.values()*kilos



def main():        
    #entrada
    frutas = {'platano':'1.35','manzana':'0.80','pera':'0.85','naranja':'0.70'}
    fruta = input("Indica la fruta que quieres: ")
    kilos = float(input("Indica ahora el peso en kilogramos que quieres: "))
    #proceso
    precio = precioTotal(frutas,fruta,kilos)
    #salida
    if fruta in frutas:
        print("El precio por " + str(kilos) + " kilos es: " + str(precio))
    else:
        "La fruta no existe."

if __name__=="__main__":
    main()