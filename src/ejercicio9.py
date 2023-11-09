'''Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.'''
#queda imprimir la cantidad cobrada hasta el momento(valor de diccionario) y lo pendiente de cobro
    
def añadirNuevaFactura(facturas:dict,nuevaFactura:str) ->dict:
    '''incluye una nueva factura en facturas
    
    Args:
        facturas(dict): diccionario donde se ingresan las facturas guardadas por el usuario
        nuevaFactura(str): facturas nuevas ingresadas por el usuario
        
    Returns:
        devuelve el conjunto de facturas ingresadas.'''
    
    factura = nuevaFactura.split(":")
    facturas[factura[0]] = factura[1]
    return facturas

def cantidadPendienteDeCobro(facturas:dict) ->str:
    '''calculamos la cantidad de facturas que faltan por pagar(las que no se han eliminado del diccionario)
    
    Args:
        facturas(dict):diccionario o conjunto de facturas
        
    Return:
        devuelve el valor de cada clave o factura'''
    
    total = 0
    for factura in facturas.values():
        total += factura
    return total
    

def procesoPagarFactura(facturas:dict,codigoFactura:str) ->dict:
    '''elimina una factura en facturas
    
    Args:
        facturas(dict): diccionario donde se ingresan las facturas guardadas por el usuario
        facturaImpagada(str): facturas a eliminar por el usuario
        
    Returns:
        devuelve el conjunto de facturas sin las pagadas.'''
    
    if codigoFactura in facturas:
        del facturas[codigoFactura]
        return("La factura se ha pagado.")
    else:
        return ("La factura no existe.")


def main():
    '''programa principal'''
    #entrada y proceso
    facturas = {}
    salir = "0"
    añadirFactura = "1"
    pagarFactura = "2"
    entrada = ""
    while entrada != salir:
        entrada = input("Indica qué quiere hacer: ")
        if entrada == añadirFactura:
            nuevaFactura = input("Indica el número de factura y su coste (separado por : ): ")
            añadida = añadirNuevaFactura(facturas,nuevaFactura)
            print(añadida)
            print("Factura añadida.")
        elif entrada == pagarFactura:
            codigoFactura = input("Indica el número de la factura: ")
            pagada = procesoPagarFactura(facturas,codigoFactura)
            print(pagada)
        #salida
        elif entrada == salir:
            print("Lo que falta por cobrar es: " + str(cantidadPendienteDeCobro(facturas)) + " .Fin.")

        else:
            print("No existe esa opción.")
    


if __name__=="__main__":
    main()