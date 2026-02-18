class alumno:
    #instanciar un alumno
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} {self.apellidos} y tengo {self.edad} años."
        