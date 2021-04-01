import random

print("---------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("---------------------------------")

numero_secreto = random.randrange(1,51)

#Contador
rodada = 1

#Selecionar dificuldade
print("1 - Fácil | 2 - Médio | 3 - Difícil ")
dificuldade = int(input("Digite um número de 1 a 3 para selecionar o nível de dificuldade: "))
if (dificuldade == 1):
    total_tentativas = 15
if (dificuldade == 2):
    total_tentativas = 10
if (dificuldade == 3):
    total_tentativas = 5
if (dificuldade < 1 or dificuldade > 3):
    print("Dificuldade inválida!Jogo Encerrado!!")
    total_tentativas = 0
#Main
for rodada in range (1,total_tentativas + 1):
    print("** Tentativa {} de {} **".format(rodada,total_tentativas))
    chute = int(input("Digite um número de 1 á 50: "))
    if (chute < 1 or chute > 50):
        print("Você deve digitar um número entre 1 e 50: ")
        continue;
    if (total_tentativas <= rodada):
        print("Suas tentativas acabaram! O número secreto era {}!".format(numero_secreto))
        break;
    if (chute == numero_secreto):
        print("Você acertou! O número secreto era {}.".format(numero_secreto))
        break;
    else:
        if(chute > numero_secreto):
            print("Você errou!! O número secreto era menor.")
        elif(chute < numero_secreto):
            print("Você errou!! O número secreto era maior.")

print("FIM DO JOGO")