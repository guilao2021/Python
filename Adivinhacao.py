import random

def jogar ():
    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")

    #Variáveis
    numero_secreto = random.randrange(1,51)
    rodada = 1
    total_tentativas = 0
    pontuacao = 500
    pontos_perdidos = 0

    #Selecionar dificuldade
    print("1 - Fácil | 2 - Médio | 3 - Difícil ")
    dificuldade = int(input("Digite um número de 1 a 3 para selecionar o nível de dificuldade: "))
    if (dificuldade == 1):
        total_tentativas = 15
    elif (dificuldade == 2):
        total_tentativas = 10
    else:
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
        elif (total_tentativas <= rodada):
            print("Suas tentativas acabaram! O número secreto era {}! E Sua pontuação foi 0!".format(numero_secreto))
            break;
        elif (chute == numero_secreto):
            print("Você acertou! E a sua pontuação foi de {} pontos!".format(pontuacao))
            break;
        else:
            if(chute > numero_secreto):
                print("Você errou!! O número secreto era menor.")
            elif(chute < numero_secreto):
                print("Você errou!! O número secreto era maior.")
            pontos_perdidos = abs(chute - pontos_perdidos)
            pontuacao = pontuacao - pontos_perdidos

    print("**FIM DO JOGO**")

if (__name__ == "__main__"):
    jogar()