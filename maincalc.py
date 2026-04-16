# Proyecto personal CALCULADORA cuenta propinas

# Fecha: 24/02/2026

# Version: 1.10

import emoji
from module import Cleaner


result = []

error = []


def Calculator(result, error):
    
    
    
    while True: #bucle infinito que mantiene la calculadora en funcionamiento
        
        print("""
█▀█ █▄█ █▀▄▀█ █▀█ █▄█ ▄▀█   █▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ ░█░ █░▀░█ █▄█ ░█░ █▀█   █▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄""")
        print("\n ➕ . Sum")
        print(" ➖ . Resta")
        print(" ✖️  . Multiplication")
        print(" ➗ . Division ")
        print(" ©️  . Clear ")
        print(" 📴 . OFF ")

        
        try: # Try para controlar los errores.
            
            
            if not error: # condicion que comprueba si hay algun error desde la ultima vez que se ejecuto el codigo
                pass
            
            else:
                print(error) # en caso de existir, se muestra el error
                
                error = [] # Volvemos a limpiar el error para que no se muestre infinitamente
                pass
            
            if not result: #Condicion para determinar si el usuario debe ingresar un numero por primera vez en caso de que result no contenga nada
                print(f"\n 🟰   0")
                num1 = int(input("\nDigite el numero: "))
                
            else: # si result contiene algo lo mostramos como el numero uno para que se reutilize
                
                num1 = result
                
                print(f"\n 🟰  {result}")
                
            
            option_choosen = input("\nChoose an Option:   ").upper() #Esta variable almacena la opcion seleccionada por el usuario para ser utilizada
            
            
            if option_choosen == '+': #Condiciones que nos llevan a la operacion realizada por el usuario.
                num2 = int(input("\nDigite el numero: "))
                
                result = num1 + num2
            
            elif option_choosen == '-': #condicion para resta
              
                num2 = int(input("\nDigite el numero: "))
                
                result = num1 - num2
                   
            elif option_choosen == '*': #Condicion que ejecuta la Multiplicacion
                
                num2 = int(input("\nDigite el numero: "))
                
                result = num1 * num2           
            
            elif option_choosen == '/': #Condicion que ejecuta la Division
                
                num2 = int(input("\nDigite el numero: "))
                
                result = num1 / num2     
            
            elif option_choosen == 'C': #Condicion para colocar los resultados en 0
                if not result:
                   result = 0
                else:
                   result - result[-1]   

            elif option_choosen == 'OFF': #Condicion que reinicia la consola
                result = 0
                Cleaner()
                break
                
                      
            
            Cleaner()
            
                
                
        except ValueError: # Error que se almacena en la lista ERROR para mostrarle al usuario
            error = '\n𝑺𝒚𝒏𝒕𝒂𝒙𝑬𝒓𝒓𝒐𝒓'
            Cleaner()
            
            
            
# code Startline


Calculator(result, error)            