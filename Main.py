import pacientes
import arbol_gral
import arbol
import historial_de_tratamiento
import generador_grafo_lista
import maxheap
import os
import time
opcion = None
os.system("cls")

print ("__________________________________________________________")
print ("___________________bienvenido al sistema__________________")
print ("_____________________de gestion medico____________________")
print ("__________________________________________________________")

time.sleep(2)
os.system("cls")
while opcion !=0:
    print ("__________________________________________________________")
    print ("____________¿que operacion desea realizar?________________")
    print ("__________________________________________________________")
    print ("__________________________________________________________")


    print ("_1. ingresar al menu pacientes____________________________")
    print ("_2. ingresar al menu de hospitales________________________")
    print ("_3. administrar sala de espera____________________________")
    print ("_0. cerrar el programa____________________________________")
    print ("_ingrese una de las opciones para continuar______________\n")

    opcion = int(input("una vez ingresado presione enter "))

    if opcion == 1:
        pass
    elif opcion ==2:
        pass
    elif opcion ==3:
        pass
    elif opcion ==0:
        pass
    else:
        os.system("cls")
        print(F"{opcion} no esta entre las opciones, vuelve a elegir una")
        opcion = 1