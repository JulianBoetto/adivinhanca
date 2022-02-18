import random

print('*********************************')
print('Bem vindo no jogo de adivinhação!')
print('*********************************')

numero_secreto = random.randrange(1,101)
total_de_tentativas = 5
rodada = 1
pontos = 100

print('Qual nível de dificultade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Defíne o nível: '))
nivel_definicao = ''

if(nivel == 1):
    total_de_tentativas = 10
    nivel_definicao = 'fácil'
elif(nivel == 2):
    total_de_tentativas = 6
    nivel_definicao = 'médio'
else:
    total_de_tentativas = 3
    nivel_definicao = 'difícil'

print('Jogando no nível {}'.format(nivel_definicao))

while (rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada,total_de_tentativas))
    chute_str= input('Digite o seu número entre 1 e 100: ')
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print('Você deve digitar entre 1 e 100!')
        continue

    print('Você digitou ', chute_str)


    acertou = numero_secreto == chute
    maior = numero_secreto<chute
    menor = numero_secreto>chute

    if(acertou):
        print('Você acertou! e fez {}'.format(pontos))
        break
    else:
        if(maior):
            print('O número é menor')
        elif(menor):
            print('O número é maior')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    rodada = rodada + 1

print('Fim do jogo')