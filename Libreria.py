import os
import math
xyz = ["X", "Y", "Z"]  # Lista con string para representacion
lista_particulas = []  # Lista que tendra la carga de todas las particulas segun el usuario
vector_particula = []  # Para el valor del vector en cada particula x
k = 9e+9  # Cosntante K con valor 9x10 ^9


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
                "las opciones validas son numeros como 1,2,3...10 , decimal o letras"


def clear_screen():   # Funcion para limpiar la pantalla dependiendo del sistema Operativo, sea Unix/mac o Windows /DOS

    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")

# Funcion que pide el numbero de particulas e imprime en pantalla de forma ordenada ademas de almacenar en las lsitas
# Correspondientes


def pedir_particulas():

    numbero_particuasl = input("Ingresa el numbero de particulas:")
    for x in range(numbero_particuasl):  # Dependiendo del numero de particulas ingresado se repetira el ciclo
        print("|-------------------------------------------|")
        carga = input("Ingresa la carga No " + str(x + 1) + ": (# e +/- #): ")
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


def numero_elementos_lista_particulas():  # Funcion que regresa el numero de elementos que tiene mas 1
    numero = len(lista_particulas)
    return numero

# -------------------------------------------Calculo de Fuerza o campo Magentio ---------------------------------------

suma_vecotres = [] # Lista para la suma de vector
def vector_resultante():

    Resultado = 0
    for particula in range(numero_elementos_lista_particulas()-1):
        raiz = 0
        cuadrado = 0
        for x in range(3):
            vector = (vector_particula[(x+3)+(particula*3)]) - (vector_particula[x]) # Se toma el valor de la carga 1 y 2, y  se restan
            suma_vecotres.append(vector) # Se agregan a una nueva lista
        clear_screen()
        print("|------------suma vecotres----------------|")
        for y in range(3): # Se suman todos los valores al caudrado
            print (xyz[y] + " = " + str(suma_vecotres[y+(particula*3)]))
            cuadrado = cuadrado + suma_vecotres[y+(particula*3)] ** 2
            raiz = math.sqrt(cuadrado) # Se saca la raiz del resultado de la suma (todos al cuadrado)
            raiz = float(raiz)
        print("|------------Valores----------------|")

        print "k  = " + str(k)
        print "Q1 =" + str(lista_particulas[0])
        print "Q2 = " + str(lista_particulas[particula+1])
        print "Raiz al cubo = " + str(raiz**3)
        print("|------------Resultado----------------|")
        for z in range (3):

            F =  (( k*(lista_particulas[0])*(lista_particulas[particula+1])) *suma_vecotres[z+(particula*3)])/raiz**3 # Se aplica la formula
            print xyz[z] + " = " + str(F)
        Resultado = Resultado + F # Resultado Final








