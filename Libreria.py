import os

xyz = ["X", "Y", "Z"]

# --------------------------Seccion de Menus y partes Graficas de bajo nivel-------------------------------------------


def menu():
    print("|------Menu------------------|")
    print("| 1. Calculate Force         |")
    print("| 2. Calculate Field         |")
    print("| 3. Exit                    |")
    print("|----------------------------|")

# ---------Fin de la seccion  de Menus y partes Graficas de bajo nivel, inicio de funciones y procedimientos-----------


def lee_si_es_nuemero():
    # Se repetira hasta llegar al return
    while True:
        opcion = raw_input("Ingrese la Opcion deseada: ")
        try:
            # Al poner el int aseguramos que sea entero si no lo es, entra al caso esepcion y repite el ciclo
            opcion = int(opcion)
            return opcion
        except ValueError:
            print "Has ingresado una opcion no valida, intentalo otra vez por favor"\
                "las opciones validas son numeros como 1,2,3...10, no se pueden negativos , decimal o letras"


def clear_screen():   # Funcion para limpiar la pantalla dependiendo del sistema Operativo, sea Unix/mac o Windows /DOS

    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")


def pedir_particulas():
    lista_particulas = []  # Lista que tendra la carga de todas las particulas segun el usuario
    vector_particula = []  # Para el valor del vector en cada particula
    numbero_particuasl = input("Ingresa el numbero de particulas:")
    for x in range(numbero_particuasl):  # Dependiendo del numero de particulas ingresado se repetira el ciclo
        print("|-------------------------------------------|")
        carga = input("Ingresa la carga No " + str(x + 1) + ": ")
        lista_particulas.append(carga)  # Agregar en lista
        for y in range(3):  # Ingresa los varlores de x,y,z para la carga correspondiente
            vector = input("Ingrese valor en " + xyz[y] + ": ")
            vector_particula.append(vector)  # Agregar en lista
    clear_screen()
    # Impresion de particulas
    for x in range(numbero_particuasl):
        print("|-----------------------------------------|")
        print ("Particula " + str(x + 1))
        print ("Carga = " + str(lista_particulas[x]))  # Llamara de la lista_particulas el valor en x
        for y in range(3):
            print (xyz[y] + " = " + str(
                vector_particula[y + (x * 3)]))  # Llamara de la lsita vecotr el valor en x*r
            # De esta manera se asegura que sea de la carga correcta
    print("|-----------------------------------------|")
