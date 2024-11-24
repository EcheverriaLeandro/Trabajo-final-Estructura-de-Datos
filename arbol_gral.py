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