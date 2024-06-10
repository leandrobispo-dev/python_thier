import random


# Passo 1: Escolher uma Palavra Aleatória
def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "logica", "programacao", "tendencias"]
    return random.choice(palavras)


# Passo 2: Criar a Função de Exibir a Forca
def exibir_forca(tentativas):
    estagios = [
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """
    ]
    print(estagios[tentativas])


# Passo 3: Iniciar o Jogo
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_" for _ in palavra]
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    exibir_forca(tentativas)
    print("Palavra:", " ".join(palavra_oculta))
    print("\n")

    # Passo 4: Loop Principal do Jogo
    while True:
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Entrada inválida. Por favor, digite uma única letra.")
            continue

        if tentativa in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(tentativa)

        if tentativa in palavra:
            for indice, letra in enumerate(palavra):
                if letra == tentativa:
                    palavra_oculta[indice] = tentativa
            print("Acertou!")
        else:
            tentativas += 1
            print("Errou!")

        exibir_forca(tentativas)
        print("Palavra:", " ".join(palavra_oculta))
        print("Letras tentadas:", " ".join(letras_tentadas))
        print("\n")

        # Passo 5: Verificação de Vitória e Derrota
        if "_" not in palavra_oculta:
            print("Parabéns, você ganhou! A palavra era:", palavra)
            break
        elif tentativas == 6:
            print("Você perdeu! A palavra era:", palavra)
            break

    # Passo 6: Finalização do Jogo
    print("Obrigado por jogar!")


# Função Principal para Iniciar o Jogo
if __name__ == "__main__":
    jogar()
