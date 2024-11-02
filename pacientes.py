class Pacientes:
    contador_id = 0
    
    def __init__ (self, nombre, edad):
        Pacientes.contador_id =+1
        self.nombre = nombre
        self.edad = edad
        self.historial= []
        self.medicamento= []
        self.id = Pacientes.contador_id
        
    def agregar_diagnostico (self, enfermedad):
        self.historial.append (enfermedad)


    def modificar_edad (self, nueva_edad):
        self.edad = nueva_edad 
        print (f"edad de {self.nombre} ha sido modificada a {self.edad} años")
    
    def mostrar_informacion(self):
        print(f"Paciente ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}")


