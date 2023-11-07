'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato  donde <mes> es el nombre del mes.'''


def convertirFechaEnLista(fecha:str) ->list:
    '''Convertimos la fecha introducida por el usuario en una lista.

    Params:
        fecha(str): fecha introducida por el usuario.

    Returns:
        list: donde se almacena el dia, mes y año por separado. Comprueba si es numero y si no lo es devuelve vacío.
    '''

    fecha = fecha.split('/')
    for numeros in fecha:
        if numeros.isdigit():
            return fecha
        else:
            fecha = []
            return fecha


def main():
    #entrada
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    fecha = input("Indica una fecha con el (formato dd/mm/aaa): ")
    #proceso
    diaMesAnio = convertirFechaEnLista(fecha)
    #salida
    print(str(diaMesAnio[0])+" de "+ (meses.get(int(diaMesAnio[1]))) + " de " + str(diaMesAnio[2]))

if __name__=="__main__":
    main()