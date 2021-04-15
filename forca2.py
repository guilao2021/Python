import random

def jogar():
    #variaveis
    enforcou = False
    acertou = False
    erros = 0
    total_tentativas = 7

    def bem_vindo():
        print("---------------------------------")
        print("***Bem vindo ao jogo de Forca!***")
        print("---------------------------------")

    def pede_chute():
        chute = input("Chute uma letra? ")
        chute = chute.strip().upper()
        return chute

    def func_palavra_secreta():
        palavras = []

        with open("frutas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

    def func_letras_certas(palavra_secreta):
        return ['_' for letra in palavra_secreta]

    def forca(erros):
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    def perdedor(palavra_secreta):
        print("A palavra secreta era {}".format(palavra_secreta))
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
        print("Você foi enforcado!")

    def vencedor():
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
        print("Parabéns, você ganhou!")

    #main
    bem_vindo()

    palavra_secreta = func_palavra_secreta()

    letras_certas = func_letras_certas(palavra_secreta)

    print(letras_certas)

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_certas[posicao] = letra
                posicao += 1
        else:
            erros += 1
            print("Errou a letra! Você tem mais {} tentativa(s)...".format(total_tentativas - erros))
            forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_certas
        print(letras_certas)

    if (acertou):
        vencedor()
    else:
        perdedor(palavra_secreta)

if (__name__ == "__main__"):
    jogar()





