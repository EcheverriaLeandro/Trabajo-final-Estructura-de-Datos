class EventoMedico: 
    def __init__(self, tipo, descripcion, id_evento):
        self.id = id_evento

    def mostrar_evento (self): 
        print (f"id{self.id}")
    
class ArbolBinario: 
    def __init__(self):
        self.raiz is None
    def  agregar_evento (self, id_evento): 
        nuevo_evento = EventoMedico (id_evento)
        if self.r
            