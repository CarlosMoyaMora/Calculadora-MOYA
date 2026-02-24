# Proyecto personal CALCULADORA cuenta propinas

# Fecha: 24/02/2026

# Version: 0.01


result = []

error = []


def calculadora(result, error):
    
    print("_______________Calculator pymoya________________")
    print("+. Sum")
    print("-. Resta")
    print("+. Multiplication")
    print("+. Division ")
    
    
    while True:
        try:
            if not result:
                
                num1 = int(input("\nDigite el numero: "))
            
            else:
                num1 = result
                print(f"\n Result: {num1}")
                
            
            option_choosen = input("Choose an Option:   ")
            
            if option_choosen == '+':
                
                num2 = int(input("\nDigite el numero: "))
                
                result = num1 + num2
                
                       
                
                
                
        except ValueError:
            error = 'SyntaxError'
            
            
            
            
# code Start Line


calculadora(result, error)            