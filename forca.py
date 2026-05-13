import random # Importa a biblioteca para escolher palavras aleatórias

def exibir_cabecalho(erros):

    print(f"{'JOGO DA FORCA':^30}") 
    desenhar_forca(erros) 

def jogar():
    palavras = ['ALGORITMO', 'PYTHON', 'VARIAVEL', 'INTERFACE', 'BIBLIOTECA', 'CATITO', 'DEPRESSAO', 'FACULDADE'] 
    palavra_secreta = random.choice(palavras) 
    letras_acertadas = ["_" for _ in palavra_secreta] 
    letras_tentadas = [] 
    erros = 0       

    while erros < 6 and "_" in letras_acertadas: 
        exibir_cabecalho(erros)
        
        print(f"\nPalavra:  {' '.join(letras_acertadas)}") 
        print(f"Letras usadas: {', '.join(letras_tentadas)}") 

        chute = input("Digite uma letra: ").upper().strip()

      
        if not chute or len(chute) > 1 or chute in letras_tentadas:
            continue

        letras_tentadas.append(chute) 

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[i] = letra
        else:
            erros += 1

    exibir_cabecalho(erros) 
    if "_" not in letras_acertadas:
        print(f"\nLACROU! A palavra era: {palavra_secreta}")
    else:
        print(f"\nPERDEU BETINHA! A palavra era: {palavra_secreta}")

def desenhar_forca(erros):
    estagios = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]
    print(estagios[erros])

if __name__ == "__main__":
    jogar()