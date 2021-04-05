def jogar():
    print("---------------------------------")
    print("***Bem vindo ao jogo de Forca!***")
    print("---------------------------------")

    # variaveis
    enforcou = False
    acertou = False
    tentativas = 1
    total_tentativas = 5

    palavra_secreta = "banana".lower()
    letras_acertadas = len(palavra_secreta) * ['_']

    print("Você tem {} tentativas...".format(total_tentativas))
    print(letras_acertadas)

    # main
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().lower()

        if (chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[posicao] = letra
                posicao += 1
            print("Acertou a letra! Você tem mais {} tentativa(s)...".format(total_tentativas - tentativas))
            tentativas += 1

        elif(total_tentativas >= 0):
            print("Você errou e tem mais {} tentativa(s)...".format(total_tentativas - tentativas))
            tentativas += 1
        else:
            tentativas += 1
        enforcou = tentativas > total_tentativas
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Parabéns!! Você ganhou!!!")
    else:
        print("Você perdeu!!!")

    print("**FIM DO JOGO**")

if (__name__ == "__main__"):
   jogar()

