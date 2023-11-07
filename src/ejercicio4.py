'''Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
import calendar #la funcion de calendar llamada isleap comprueba si el año es bisiesto.

LONGITUD_ANO = 4
LONGITUD_DIAMES = 2

def comprobarFormatoAnioOK(anio:str,LONGITUD_ANO:int) ->bool:
     
     '''Comprobamos si el año introducido por el usuario tiene el formato correcto.
     
    Args:
        fechaDelUsuario(str): fecha introducida por el usuario.

    Returns:
        str: si la fecha es True es correcta, si es False el caso contrario.
    '''
     
    if len(anio) == LONGITUD_ANO:
        return True
    else:
        return False
    
    


def main():
    #entrada
    fecha = {"dia":'dd','mes':'mm','año':'aaaa'}
    dia = input("Indica el día: ")
    mes = input("Indica el mes: ")
    anio = input("Por último indica el año: ")
    #proceso
    fechaCorrecta = comprobarFecha(dia,mes,año,fecha)
    #salida
    print("La fecha es: día "+ dia + ", el mes es " + mes + ", y el año " + año)

if __name__=="__main__":
    main()