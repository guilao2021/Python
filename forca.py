import random

def jogar():
    #variaveis
    enforcou = False
    acertou = False
    tentativas = 1

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

    def dificuldade():
        print("1 - Fácil | 2 - Médio | 3 - Difícil ")
        dificuldade = int(input("Digite um número de 1 a 3 para selecionar o nível de dificuldade: "))

        if (dificuldade == 1):
            print("Dica: é uma fruta")
            total_tentativas = 20
            return total_tentativas
        elif (dificuldade == 2):
            print("Dica: é uma fruta")
            total_tentativas = 12
            return total_tentativas
        elif (dificuldade == 3):
            total_tentativas = 8
            return total_tentativas
        else:
            enforcou = True
            total_tentativas = 0
            return total_tentativas

    #main
    bem_vindo()

    palavra_secreta = func_palavra_secreta()

    letras_certas = func_letras_certas(palavra_secreta)

    total_tentativas = dificuldade()

    print("Você tem {} tentativas...".format(total_tentativas))
    print(letras_certas)

    while (not enforcou and not acertou):
            chute = input("Qual a letra? ")
            chute = chute.strip().upper()

            if (chute in palavra_secreta):
                posicao = 0
                for letra in palavra_secreta:
                    if (chute == letra):
                        letras_certas[posicao] = letra
                    posicao += 1
                print("Acertou a letra! Você tem mais {} tentativa(s)...".format(total_tentativas - tentativas))
                tentativas += 1

            elif(total_tentativas >= 0):
                print("Você errou e tem mais {} tentativa(s)...".format(total_tentativas - tentativas))
                tentativas += 1
            else:
                tentativas += 1
            enforcou = tentativas > total_tentativas
            acertou = '_' not in letras_certas
            print(letras_certas)

    if (acertou):
        print("Parabéns!! Você ganhou!!!")
    else:
        print("Você perdeu!!!A palavra secreta era {} !".format(palavra_secreta))

if (__name__ == "__main__"):
    jogar()






