from pacientes import Pacientes


class NodoPaciente: 
    def __init__ (self, paciente): 
        self.paciente = paciente
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVLPacientes: 
    def __init__ (self):
        self.raiz = None

    def arbol_vacio(self):
        if self.raiz is None:
            return True
    
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.derecho) - self.obtener_altura(nodo.izquierdo)
    
    def rotar_derecha(self, nodo):
        nueva_raiz = nodo.izquierdo
        arbol_derecho_auxiliar = nueva_raiz.derecho
        nueva_raiz.derecho = nodo
        nodo.izquierdo = arbol_derecho_auxiliar
        
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo), self.obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.obtener_altura(nueva_raiz.izquierdo), self.obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz
    
    # def insertar (self, paciente):  #metodo publico
    #     nuevo_nodo = NodoPaciente (paciente) 
    #     if self.arbol_vacio == True:
    #         self.raiz = nuevo_nodo
    #     else: 
    #         self.__insertar_nodo (self.raiz, nuevo_nodo) 

    # def __insertar_nodo (self, nodo_actual, nuevo_nodo): #Metodo privado
    #     if nuevo_nodo.paciente.id < nodo_actual.paciente.id:
    #         if nodo_actual.izquierdo is None: 
    #             nodo_actual.izquiedo = nuevo_nodo
    #         else: 
    #             self.__insertar_nodo (nodo_actual.izquierdo, nuevo_nodo) 
    #     else:
    #         if nodo_actual.derecho is None: 
    #             nodo_actual.derecho = nuevo_nodo
    #         else: 
    #             self.__insertar_nodo (nodo_actual.derecho, nuevo_nodo)

    def buscar (self, id_paciente): 
        return self.__buscar_paciente (self.raiz, id_paciente)
    
    def __buscar_paciente (self, nodo_actual, id_paciente):
        if nodo_actual is None: 
            return None
        if nodo_actual.paciente.id == id_paciente:
            return nodo_actual.paciente
        elif id_paciente < nodo_actual.paciente.id:
            return self.__buscar_paciente (nodo_actual.izquierdo, id_paciente)
        else: 
            return self.__buscar_paciente (nodo_actual.derecho, id_paciente)