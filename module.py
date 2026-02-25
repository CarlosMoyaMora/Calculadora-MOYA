import os


def Cleaner(): #funcion para limpiar consola
    
    clean = 'cls' if os.name == 'nt' else 'clear'
    os.system(clean)