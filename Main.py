"""
*
-----------------------------------
*Name : Jose Carlos Pacheco Sanchez
*ID :A01702828
-----------------------------------
*Date : 17 August 2018
*Subject : Electricity and Mangetism
*OS Enviorment : Mac OS Sierra 10.13.6 build
* Developed on Pycharm PyCharm 2018.2.1 (Professional Edition) Build #PY-182.3911.33
*
"""

# Libraries
import time
import os
import Libreria

# End Libraries

opcion = 0
while opcion != 7:
        Libreria.clear_screen()
        Libreria.menu()  # Mostrar menu
        opcion = Libreria.lee_si_es_nuemero()
        # Programa numero uno
        if opcion == 1:
            Libreria.clear_screen()
            print("Calculo de Fuerza Magnetica")
            time.sleep(3)
        elif opcion == 2:
            print("Calulo de Campo Magnetico")
            time.sleep(3)

        else:
            break
print("Fin programa")
