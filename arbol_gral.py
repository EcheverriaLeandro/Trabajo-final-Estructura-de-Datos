from pacientes import Pacientes

class NodoGeneral:
    def __init__(self, evento):
        self.evento = evento      # InformaciÃ³n del nodo
        self.hijos = []           # Lista de hijos
        self.hermano = None       # Referencia al siguiente nodo hermano

    def agregar_hijo(self, nodo_hijo):    
        self.hijos.append(nodo_hijo) #agregamos un nodo hijo a la raiz 

    def agregar_hermano(self, nodo_hermano):
        self.hermano = nodo_hermano #agregamos nodo hermano al primer nodo

#debido a la consigna vamos a obviar la existencia de nodo raiz hijos y hermanos pues esos nodos ya existen y el primer nodo hijo es primer consulta (que esta asociado a la primer visita) y el segundo nodo el cual seria su nodo hermano seria segunda consulta. estos nodos a su vez tienen dos nodos hijos que son diagnostico y tratamiento 
class ArbolGeneral:
    def __init__(self, evento_raiz):
        self.raiz = NodoGeneral(evento_raiz)  # la raiz siempre sera evento raiz

    def agregar_hijo(self, nodo_padre, evento_hijo):
        #Agregamos el primer hijo
        nodo_hijo = NodoGeneral(evento_hijo)
        nodo_padre.agregar_hijo(nodo_hijo)
        return nodo_hijo

    def agregar_hermano(self, nodo, evento_hermano):
        #agregamos un hermano al primer hijo
        nodo_hermano = NodoGeneral(evento_hermano)
        nodo.agregar_hermano(nodo_hermano)
        return nodo_hermano

    def imprimir_arbol_con_hermanos(self, nodo, nivel=0):
        #imprime el nodo considerando hijos y hermanos 
        while nodo:
            print("  " * nivel + f"- {nodo.evento}")
            for hijo in nodo.hijos:
                self.imprimir_arbol_con_hermanos(hijo, nivel + 1)
            nodo = nodo.hermano
    
paciente1 = Pacientes("Juan Pérez", 65)

# Construccion del arbol con hijos y hermanos
arbol = ArbolGeneral(paciente1)  #raiz

# nivel 1 
consulta_1 = arbol.agregar_hijo(arbol.raiz, "Primer consulta")
consulta_2 = arbol.agregar_hermano(consulta_1, "Segunda consulta")

# nivel 2 hijos y hermanos para consulta 2 
diagnostico_1 = arbol.agregar_hijo(consulta_1, "Primer diagnostico")
tratamiento_1 = arbol.agregar_hermano(diagnostico_1, "Primer tratamiento")

# nivel 2 hijos y hnos para consulta 2 
diagnostico_2 = arbol.agregar_hijo(consulta_2, "Segundo diagnostico")
tratamiento_2 = arbol.agregar_hermano(diagnostico_2, "Segundo tratamiento")

arbol.imprimir_arbol_con_hermanos(arbol.raiz)
