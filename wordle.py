import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKGREY = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print('*********************************')
print('      Bienvenidos a wordle!')
print('*********************************')

# print(bcolors.OKGREEN + "verde" + bcolors.ENDC)
# print(bcolors.FAIL + "rojo" + bcolors.ENDC)

palabras = ["marca","birra","torta","perro"]

palabra_hoy = random.choice(palabras)

print('Escribe una palabra de 5 letras')
intentos = 0
oportunidades = 5
n = 0

palabra_print = []

while(intentos < oportunidades):
    palabra = str(input())
    palabra_valida = len(palabra) == 5  
    if(palabra_valida):
        if(palabra == palabra_hoy):
            print(bcolors.OKGREEN + letra + bcolors.ENDC + ' Adiviniste la palabra!')
            break
        else:
            for letra in palabra:
                if(letra == palabra_hoy[n]):
                    print(bcolors.OKGREEN + letra + bcolors.ENDC)
                else:
                    if(palabra_hoy.find(letra) > 0):
                        print(bcolors.OKBLUE + letra + bcolors.ENDC)                        
                    else:
                        print(bcolors.OKGREY + letra + bcolors.ENDC)
                n = n + 1
                # palabra_print.append(letra)
            n = 0
            # print(palabra_print)
        intentos = intentos + 1
    else:
        print('Ingresa una palabra de 5 letras')  
