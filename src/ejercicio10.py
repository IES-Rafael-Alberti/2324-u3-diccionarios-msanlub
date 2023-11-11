'''Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

    1.Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    2.Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3.Preguntar por el NIF del cliente y mostrar sus datos.
    4.Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5.Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    6.Terminar el programa.
'''

def agregaClienteNuevo(baseDatos:dict,nif:str) ->dict:
    '''
    Agregamos los datos de cliente nuevo en dos diccionarios(NIF diccionario principal; nombre,dirección,teléfono,correo,preferente en el secundario)

    Parameters
    ----------

    baseDatos(dict): almacenamos datos de los clientes segun su nif
    
    nif(str): nif ingresado por el usuario

    Returns
    -------

    '''
    cliente = {}
    nombre = input('Introduce el nombre del cliente: ')
    cliente['nombre'] = nombre
    direccion = input('Introduce la dirección del cliente: ')
    cliente['dirección'] = direccion
    telefono = input('Introduce el teléfono del cliente: ')
    cliente['teléfono'] = telefono
    email = input('Introduce el correo electrónico del cliente: ')
    cliente['email'] = email
    preferente = input('Indique si es cliente preferente (S/N): ')
    if preferente == 'S':
        cliente['preferente']=True
    else: 
        cliente['preferente']=False
    baseDatos[nif] = cliente
    return baseDatos


def eliminarCliente(baseDatos:dict,eliminarNif:str):
    '''
    Eliminar los datos de cliente según su nif ingresado por el usuario

    Parameters
    ----------

    baseDatos(dict): datos clientes
    
    eliminarNif(str): nif ingresado por el usuario

    Returns
    -------

    '''
        
    if eliminarNif in baseDatos:
        del baseDatos[eliminarNif]
    else:
        return ('No existe el cliente con el nif' + eliminarNif)


def accederCliente(baseDatos:dict,accesoNif:str):
    '''
    Acceder a los datos de cliente según su nif ingresado por el usuario

    Parameters
    ----------

    baseDatos(dict): datos clientes
    
    accesoNif(str): nif ingresado por el usuario

    Returns
    -------
    Los datos del cliente solicitado.
    '''
            
    if accesoNif in baseDatos:
        for clave, valor in baseDatos[accesoNif].items():
            return clave.title() + ':' + valor

def listadoClientes(baseDatos:dict) ->str:
    '''
    Listado de clientes de la base de datos.

    Parameters
    ----------

    baseDatos(dict): datos clientes

    Returns
    -------
    Todos los clientes de la base de datos
    '''

    clientes = ""
    for clave,valor in baseDatos.items():
        clientes += clave + " " + valor['nombre'] + "\n"
    return clientes

def listadoClientesPreferentes(baseDatos:dict) ->str:
    '''
    Listado de clientes preferentes de la base de datos.

    Parameters
    ----------

    baseDatos(dict): datos clientes

    Returns
    -------
    Sólo los clientes preferentes de la base de datos(keys)
    '''
    
    preferentes = ""
    for clave,valor in baseDatos.items():
        if valor['preferente'] == True:
            preferentes += str(valor['nombre']) + "\n"
    return preferentes 

def main():
    '''programa principal'''
    #entrada
    ANIADIR = "1"
    ELIMINAR = "2"
    MOSTRAR = "3"
    LISTAR = "4"
    PREFERENTES = "5"
    FIN = "6"
    baseDatos = {}
    entrada = ""
    while entrada != FIN:
        entrada = input("Elige una opción:\n\t(1) Añadir cliente\n\t(2) Eliminar cliente\n\t(3) Mostrar cliente\n\t(4) Listar todos los clientes\n\t(5) Listar clientes preferentes\n\t(6) Terminar\n\t")
        if entrada == ANIADIR:
            nif = input("Indique su NIF: ")
            agregaClienteNuevo(baseDatos,nif)
            print("Cliente agregado.")

        elif entrada == ELIMINAR:
            eliminarNif = input("Indique el NIF del cliente a eliminar: ")
            eliminarCliente(baseDatos,eliminarNif)
            print("Cliente eliminado.")

        elif entrada == MOSTRAR:
            accesoNif = input("Indica el NIF del cliente a mostrar: ")
            print(accederCliente(baseDatos,accesoNif))

        elif entrada == LISTAR:
            print(listadoClientes(baseDatos))

        elif entrada == PREFERENTES:
            print(listadoClientesPreferentes(baseDatos))
    else:
        print("Fin programa.")


if __name__=="__main__":
    main()