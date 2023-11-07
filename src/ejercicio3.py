'''Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''

def precio(frutas:dict,fruta:str) ->float:
    '''Devuelve el precio del kilo de la fruta que quiere el usuario.
     
    Args:
        frutas(dict),fruta(str)

    Returns:
        float: precio de la fruta por kilo.
    '''
    
    return frutas.get(fruta) 


def main():        
    #entrada
    frutas = {'platano':1.35,'manzana':0.80,'pera':0.85,'naranja':0.70}
    fruta = input("Indica la fruta que quieres: ")
    #proceso y salida
    if fruta in frutas:
        kilos = float(input("Indica ahora el peso en kilogramos que quieres: "))
        precioTotal = precio(frutas,fruta) * kilos
        print("El precio por " + str(kilos) + " kilos es: " + str(precioTotal))
    else:
        print("La fruta no existe.")

if __name__=="__main__":
    main()