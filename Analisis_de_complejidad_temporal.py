    
    este modulo pertenece a nuestro albol general y es del orden de O(n**2) porque tenemos ciclos anidados
    
    def imprimir_arbol_con_hermanos(self, nodo, nivel=0): #recorrido preorder 
        #imprime el nodo considerando hijos y hermanos 
        while nodo:                              -->                       O(n)
            print("  " * nivel + f"- {nodo.evento}")                               
            for hijo in nodo.hijos:              -->                       O(m)
                self.imprimir_arbol_con_hermanos(hijo, nivel + 1)
            nodo = nodo.hermano
                                                                           entonces este metodo tiene un timpo O(m*n) por lo tanto suponiendo que n>m se podria decir que su complejidad temporal es O(n**2)
    
    
_________________________________________________________________________________________________________________________________________________________________________________________________________________
    para calcular el big Oh de la insersion en nuestro arbolAVL es mas complejo porque el metodo de insersion depende de otros metodos
    
    def insersion(self, paciente): #metodo publico de insersion 
        self.raiz = self.__insertar_nodo(self.raiz, paciente)
    
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
        
    def __obtener_altura(self, nodo): #metodo necesario para obtener la altura de nuestros nodos
        if not nodo:
            return 0
        return nodo.altura
    
    def __obtener_balance(self, nodo): #metodo necesario para luego comparar el desbalance o no de nuestros nodos
        if not nodo:
            return 0
        return self.__obtener_altura(nodo.derecho) - self.__obtener_altura(nodo.izquierdo)
    
    def __rotar_derecha(self, nodo): #metodo para hacer que el hijo izquierdo sea la nueva raiz y reajusta la altura de los nodos
        nueva_raiz = nodo.izquierdo
        arbol_derecho_auxiliar = nueva_raiz.derecho
        
        nueva_raiz.derecho = nodo
        nodo.izquierdo = arbol_derecho_auxiliar
        
        nodo.altura = 1 + max(self.__obtener_altura(nodo.izquierdo), self.__obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.__obtener_altura(nueva_raiz.izquierdo), self.__obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz
    
    def __rotar_izquierda(self, nodo): #metodo para hacer que el hijo derecho sea la nueva raiz y reajusta la altura de los nodos
        nueva_raiz = nodo.derecho
        arbol_izquierdo_auxiliar = nueva_raiz.izquierdo
        
        nueva_raiz.izquierdo = nodo
        nodo.derecha = arbol_izquierdo_auxiliar
        
        nodo.altura = 1 + max(self.__obtener_altura(nodo.izquierdo), self.__obtener_altura(nodo.derecho))
        nueva_raiz.altura = 1 + max(self.__obtener_altura(nueva_raiz.izquierdo), self.__obtener_altura(nueva_raiz.derecho))
        
        return nueva_raiz
    

_________________________________________________________________________________________________________________________________________________________________________________________________________________