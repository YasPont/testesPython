import random

def jogar_adivinhacao():
    print("   BEM-VINDO AO ADIVINHADOR!   ")
    
    numero_secreto = random.randint(1, 100) 
    tentativas = 0
    max_tentativas = 10
    ganhou = False

    print(f"Estou pensando em um número de 1 a 100...")
    print(f"Você tem {max_tentativas} tentativas!")

    while tentativas < max_tentativas:
        print(f"\nTentativa {tentativas + 1} de {max_tentativas}")
        
        try:
            chute = int(input("Qual o seu palpite? "))
        except ValueError:
            print("Digite apenas números inteiros, Plase!")
            continue

        tentativas += 1

        if chute == numero_secreto:
            ganhou = True
            break
        elif chute < numero_secreto:
            print("MAIOR! O número secreto é maior que esse.")
        else:
            print("MENOR! O número secreto é menor que esse.")

    if ganhou:
        print(f"\n URUUU, PARABÉNS! Você acertou em {tentativas} tentativas!")
    else:
        print(f"\n FIM DE JOGO! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogar_adivinhacao()