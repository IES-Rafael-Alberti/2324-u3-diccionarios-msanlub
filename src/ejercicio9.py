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
    '''calculamos el total del costo de las facturas que faltan por pagar(las que no se han eliminado del diccionario)
    
    Args:
        facturas(dict):diccionario o conjunto de facturas
        
    Return:
        devuelve la cantidad que falta por cobrar (valor de las claves del diccionario)'''
    
    total = 0
    for factura in facturas:
        total += int(facturas[factura])
    return total
    

def procesoPagarFactura(facturas:dict,codigoFactura:str,facturasPagadas:dict) ->dict:
    '''elimina una factura en facturas
    
    Args:
        facturas(dict): diccionario donde se ingresan las facturas guardadas por el usuario
        codigoFactura(str): codigo de facturas a eliminar por el usuario
        
    Returns:
        devuelve el conjunto de facturas sin las pagadas.'''
    
    
    if codigoFactura in facturas:
        facturasPagadas[codigoFactura] = facturas[codigoFactura]

        del facturas[codigoFactura]
        return("La factura se ha pagado.")
    else:
        return ("La factura no existe.")


def cantidadCobrada(facturasPagadas:dict):
    '''calculamos el total que se ha cobrado de las facturas.
    
    Args:
        facturas(dict):diccionario o conjunto de facturas
        codigoFactura(str): codigo de facturas a eliminar por el usuario
        
    Return:
        la suma de valores que se han cobrado(los valores de las facturas que se eliminan del diccionario)'''
    
    total = 0
    for factura in facturasPagadas.values():
        total += int(factura)
    return total

    

def main():
    '''programa principal'''
    #entrada y proceso
    facturas = {}
    facturasPagadas = {}
    salir = "0"
    añadirFactura = "1"
    pagarFactura = "2"
    entrada = ""
    while entrada != salir:
        entrada = input("Indica qué quiere hacer: ")
        if entrada == añadirFactura:
            nuevaFactura = input("Indica el número de factura y su coste (separado por : ): ")
            añadida = añadirNuevaFactura(facturas,nuevaFactura)
            print("Factura añadida.")
        elif entrada == pagarFactura:
            codigoFactura = input("Indica el número de la factura: ")
            pagada = procesoPagarFactura(facturas,codigoFactura,facturasPagadas)
            print(pagada)
        #salida
        elif entrada == salir:
            print("Lo que falta por cobrar es: " + str(cantidadPendienteDeCobro(facturas)) + " .Lo que se ha cobrado es: " + str(cantidadCobrada(facturasPagadas)) + " .Fin")
        else:
            print("No existe esa opción.")
    


if __name__=="__main__":
    main()