class Pacientes:
    contador_id = 0
    
    def __init__ (self, nombre, edad):
        Pacientes.contador_id =+1
        self.nombre = nombre
        self.edad = edad
        self.historial= []
        self.medicamento= []
        self.id = Pacientes.contador_id
        
    def agregar_dx (self, enfermedad):
        self.historial.append (enfermedad)


    def agregar_med (self, medicamento):
        self.medicamento.append (medicamento)


    
    

    
