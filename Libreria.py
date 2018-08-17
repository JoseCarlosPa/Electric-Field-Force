import os


# --------------------------Seccion de Menus y partes Graficas de bajo nivel-------------------------------------------

def menu():
    print("|------Menu---------|")
    print("| 1. Theory         |")
    print("| 2. Program        |")
    print("| 3. Exit           |")
    print("|-------------------|")

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
