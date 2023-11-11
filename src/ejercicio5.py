'''Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.'''

def totalCreditos(curso:dict):
    '''devuelve el total de créditos
    
    Args:
        curso(dict): diccionario creado con asignaturas y los creditos
        
    Returns:
        el total de los creditos de todas las asignaturas.'''

    total = 0
    for creditos in curso.values():
        total += creditos
    return total


def main():
    #entrada
    curso = {'Matemáticas':6,'Física':4,'Química':5}
    #proceso
    totalC = totalCreditos(curso)
    for asignaturas,creditos in curso.items():
        #salida
        print(asignaturas + " tiene " + str(creditos) + " créditos.")
    print("El total de créditos es: " + str(totalC))

if __name__=="__main__":
    main()

