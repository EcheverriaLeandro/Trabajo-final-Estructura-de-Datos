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
    
    def __obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    def __obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.__obtener_altura(nodo.derecho) - self.__obtener_altura(nodo.izquierdo)
    
    def __rotar_derecha(self, nodo):
        nueva_raiz = nodo.izquierdo
        arbol_derecho_auxiliar = nueva_raiz.derecho
        nueva_raiz.derecho = nodo
        nodo.izquierdo = arbol_derecho_auxiliar
        
        nodo.altura = 1 + max(self.__obtener_altura(nodo.izquierdo), self.__obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.__obtener_altura(nueva_raiz.izquierdo), self.__obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz
    
    def __rotar_izquierda(self, nodo):
        nueva_raiz = nodo.derecho
        arbol_izquierdo_auxiliar = nueva_raiz.izquierdo
        nueva_raiz.izquierdo = nodo
        nodo.derecha = arbol_izquierdo_auxiliar
        
        nodo.altura = 1 + max(self.__obtener_altura(nodo.izquierdo), self.__obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.__obtener_altura(nueva_raiz.izquierdo), self.__obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz
    
    def __insertar_nodo (self, raiz, nuevo_nodo): #Metodo privado
        if not raiz:
            return NodoPaciente(nuevo_nodo)
        
        if nuevo_nodo.id < raiz.paciente.id:
            raiz.izquierdo = self.__insertar_nodo(raiz.izquierdo, nuevo_nodo)
        else:
            raiz.derecho = self.__insertar_nodo(raiz.derecho, nuevo_nodo)
        
        raiz.altura = 1 + max(self.__obtener_altura(raiz.izquierdo), self.__obtener_altura(raiz.derecho))
        
        balance = self.__obtener_balance(raiz)
        
        #rotacion a la derecha
        if balance > 1 and nuevo_nodo.id < raiz.izquierdo.id:
            return self.__rotar_derecha(raiz)
        #rotacion a la izquierda
        if balance < -1 and nuevo_nodo.id > raiz.izquierdo.id:
            return self.__rotar_izquierda(raiz)
        #rotacion izquierda derecha
        if balance > 1 and nuevo_nodo.id > raiz.izquierdo.id:
            raiz.izquierdo = self.__rotar_izquierda(raiz.izquierdo)
            return self.__rotar_derecha(raiz)
        #rotacion derecha izquierda
        if balance < -1 and nuevo_nodo.id < raiz.derecho.id:
            raiz.derecho = self.__rotar_derecha(raiz.derecho)
            return self.__rotar_izquierda(raiz)
    
        return raiz
    
    def insersion(self, paciente):
        self.raiz = self.__insertar_nodo(self.raiz, paciente)
        
    def __buscar_minimo(self, nodo):
        if nodo is None or nodo.izquierdo is None:
            return nodo
        return self.__buscar_minimo(nodo)
    
    def __eliminar(self, raiz, id_paciente):
        if not raiz:
            return raiz
        
        if id_paciente < raiz.id:
            raiz.izquierdo = self.__eliminar(raiz.derecho, id_paciente)
        elif id_paciente > raiz.id:
            raiz.derecho = self.__eliminar(raiz.izquierdo, id_paciente)
        else:
            if not raiz.izquierdo:
                auxiliar = raiz.derecho
                raiz = None
                return auxiliar
            elif not raiz.derecho:
                auxiliar = raiz.izquierdo
                raiz = None
                return auxiliar
            
            auxiliar = self.__buscar_minimo(raiz.derecho)
            raiz.paciente = auxiliar.paciente
            raiz.derecho = self.__eliminar(raiz.derecha, auxiliar.id)
            
        if not raiz:
            return raiz
        
        raiz.altura = max(self.__obtener_altura(raiz.izquierdo), self.__obtener_altura(raiz.derecho))
        
        balance = self.__obtener_balance(raiz)
        
        #rotacion a la derecha
        if balance > 1 and self.__obtener_balance(raiz.derecho) >= 0:
            return self.__rotar_derecha(raiz)
        #rotacion a la izquierda
        if balance < -1 and self.__obtener_balance(raiz.izquierdo) <= 0:
            return self.__rotar_izquierda(raiz)
        #rotacion izquierda derecha
        if balance > 1 and self.__obtener_balance(raiz.izquierdo) < 0:
            raiz.izquierdo = self.__rotar_izquierda(raiz.izquierdo)
            return self.__rotar_derecha(raiz)
        #rotacion derecha izquierda
        if balance < -1 and self.__obtener_balance(raiz.izquierdo) > 0:
            raiz.derecho = self.__rotar_derecha(raiz.derecho)
            return self.__rotar_izquierda(raiz)
        
        return raiz
        
    def buscar (self, id_paciente): 
        return self.__buscar_paciente(self.raiz, id_paciente)
    
    def __buscar_paciente (self, nodo_actual, id_paciente):
        if nodo_actual is None: 
            return None
        if nodo_actual.paciente.id == id_paciente:
            return nodo_actual.paciente
        elif id_paciente < nodo_actual.paciente.id:
            return self.__buscar_paciente (nodo_actual.izquierdo, id_paciente)
        else: 
            return self.__buscar_paciente (nodo_actual.derecho, id_paciente)