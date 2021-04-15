import random

def jogar():
    # Variáveis
    numero_secreto = random.randrange(1, 51)
    rodada = 1

    def ganhou():
        print("Você acertou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def perdeu(numero_secreto):
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        print("Suas tentativas acabaram! O número secreto era {}!".format(numero_secreto))

    def bem_vindo():
        print("---------------------------------")
        print("Bem vindo ao jogo de adivinhação!")
        print("---------------------------------")

    def dificuldade():
        print("1 - Fácil | 2 - Médio | 3 - Difícil ")
        dificuldade = int(input("Digite um número de 1 a 3 para selecionar o nível de dificuldade: "))
        if (dificuldade == 1):
            total_tentativas = 15
            return total_tentativas
        elif (dificuldade == 2):
            total_tentativas = 10
            return total_tentativas
        elif (dificuldade == 3):
            total_tentativas = 5
            return total_tentativas
        elif (dificuldade < 1 or dificuldade > 3):
            print("Dificuldade inválida!Jogo Encerrado!!")
            total_tentativas = 0
            return total_tentativas

    # Main
    bem_vindo()

    total_tentativas = dificuldade()
    
    for rodada in range(1, total_tentativas + 1):
        print("** Tentativa {} de {} **".format(rodada, total_tentativas))
        chute = int(input("Digite um número de 1 á 50: "))
        if (chute < 1 or chute > 50):
            print("Você deve digitar um número entre 1 e 50: ")
            continue
        else:
            if (chute > numero_secreto):
                print("Você errou!! O número secreto era menor.")
            elif (chute < numero_secreto ):
                print("Você errou!! O número secreto era maior.")

        if (chute == numero_secreto):
            ganhou()
            break
        elif (rodada >= total_tentativas):
            perdeu(numero_secreto)
            break

if (__name__ == "__main__"):
    jogar()
