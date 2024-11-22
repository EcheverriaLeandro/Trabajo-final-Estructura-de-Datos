class Nodoevento:
    def __init__ (self, tipo_evento, descripcion):
        self.tipo_evento = tipo_evento
        self.descripcion = descripcion
        self.primer_hijo = None
        self.hermano_sig = None

    def arbol_vacio (raiz):
        #retorna si el arbol esta vacio
        return raiz == None
    
    def arbol_vacio(raiz):
	#retorna si el arbol esta vacio
	    return raiz == None
	
    def agregar_hijo_raiz(raiz,info):
	#inserto el dato en el arbol
	        if arbol_vacio(raiz):
		        raiz = Nodoevento(info)
		#referencio el comienzo de la lista