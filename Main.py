"""
*
-----------------------------------
*Name : Jose Carlos Pacheco Sanchez
*ID :A01702828
-----------------------------------
*OS Enviorment : Mac OS Sierra 10.13.6 build
* Developed on Pycharm PyCharm 2018.2.1 (Professional Edition) Build #PY-182.3911.33
----------------------------------
*Name : Hugo David Franco Avila
*ID: A01654856
*Os Enviorment: Windows 10 10.0.17134.228
*Developed on Bloc de Notas
*
-----------------------------------
*Date : 17 August 2018
*Subject : Electricity and Mangetism
*
"""
# Libraries

import Libreria

# End Libraries

opcion = 0
while opcion != 3:
    Libreria.menu()  # Mostrar menu
    opcion = Libreria.lee_si_es_nuemero()
    Libreria.clear_screen()
    if opcion == 1:
        print "++Calculo Fuerza magentica++\n"
        print ("Ponga la primera particula como la particual con la que se calculara todo")
        Libreria.pedir_particulas()
        Libreria.vector_resultante()
        raw_input("\nPress Enter to conitnue")
    elif opcion == 2:
        print("Calulo de Campo Magnetico")
        Libreria.pedir_particulas()

        raw_input("\nPress Enter to conitnue")

    else:
        break
print("Fin programa")
