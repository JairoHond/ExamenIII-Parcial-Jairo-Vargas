# Importa la función num2words desde la biblioteca num2words
from num2words import num2words

# Define una función para convertir un número en su representación en palabras
def convertir_a_palabras(numero):
    # El parámetro lang='es' especifica que se debe utilizar el idioma español
    return num2words(numero, lang='es').upper()

# Define la función principal del programa
def main():
    try:
        # Solicita al usuario que ingrese un número entero
        numero = int(input("Ingrese un número entero: "))
        # Llama a la función convertir_a_palabras para obtener la representación en palabras del número ingresado
        resultado = convertir_a_palabras(numero)
       
        print(f"El número {numero} en palabras es: {resultado}")
    except ValueError:
        # Maneja la excepción si el usuario ingresa un valor que no puede convertirse a un número entero
        print("Por favor, ingrese un número entero válido.")
        
if __name__ == "__main__":
    main()

# Documentación adicional:
# Para este ejercicio se debe utilizar la biblioteca num2words ya que inflect se dice que ya está desactualizada.
# Para instalar num2words, utiliza el siguiente comando: pip install num2words
