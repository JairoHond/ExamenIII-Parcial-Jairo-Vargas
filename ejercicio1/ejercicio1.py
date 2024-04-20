import csv

class Persona:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = float(salario)
        self.deducciones = float(deducciones)
        self.genero = genero

class ProcesadorCSV:
    def __init__(self, archivo):
        self.personas = self._cargar_personas(archivo)
    
    def _cargar_personas(self, archivo):
        personas = []
        with open(archivo, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                persona = Persona(row['Nombre'], row['Apellido'], row['Edad'], row['Salario'], row['Deducciones'], row['Genero'])
                personas.append(persona)
        return personas
    
    def persona_mayor_edad(self):
        #Encuentra la persona con la mayor edad.
        return max(self.personas, key=lambda x: x.edad)
    
    def persona_menor_edad(self):
        #Encuentra la persona con la menor edad.
        return min(self.personas, key=lambda x: x.edad)
    
    def contar_genero(self):
        #Cuenta la cantidad de hombres y mujeres.
        hombres = sum(1 for persona in self.personas if persona.genero.lower() == 'masculino')
        mujeres = sum(1 for persona in self.personas if persona.genero.lower() == 'femenino')
        return hombres, mujeres
    
    def promedio_salario(self):
        #Calcula el promedio de salario de todas las personas.
        total_salario = sum(persona.salario for persona in self.personas)
        return total_salario / len(self.personas)
    
    def persona_con_mas_deducciones(self):
        """Encuentra la persona con las mayores deducciones."""
        return max(self.personas, key=lambda x: x.deducciones)
    
    def persona_con_mayor_salario(self):
        """Encuentra la persona con el mayor salario."""
        return max(self.personas, key=lambda x: x.salario)

# Uso del procesador CSV
def main():
    procesador = ProcesadorCSV('C:/Users/jairo/Desktop/ExamenIII-Parcial/ejercicio1/datos.csv')

    persona_mayor_edad = procesador.persona_mayor_edad()
    persona_menor_edad = procesador.persona_menor_edad()
    hombres, mujeres = procesador.contar_genero()
    promedio_salario = procesador.promedio_salario()
    persona_mas_deducciones = procesador.persona_con_mas_deducciones()
    persona_mayor_salario = procesador.persona_con_mayor_salario()

    print("Persona con mayor edad:", persona_mayor_edad.nombre, persona_mayor_edad.apellido)
    print("Persona con menor edad:", persona_menor_edad.nombre, persona_menor_edad.apellido)
    print("Cantidad de hombres:", hombres)
    print("Cantidad de mujeres:", mujeres)
    print("Promedio de salario:", promedio_salario)
    print("Persona con más deducciones:", persona_mas_deducciones.nombre, persona_mas_deducciones.apellido)
    print("Persona con mayor salario:", persona_mayor_salario.nombre, persona_mayor_salario.apellido)

if __name__ == "__main__":
    main()
