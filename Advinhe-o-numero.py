import random

def main():
    print("Bem-vindo ao jogo de adivinhar números!")
    print("Eu vou escolher um número aleatório entre 1 e 100, e você tem que adivinhar qual é.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while True:
        tentativas += 1
        palpite = int(input("Digite o seu palpite: "))
        
        if palpite < numero_secreto:
            print("O seu palpite é menor do que o número secreto.")
        elif palpite > numero_secreto:
            print("O seu palpite é maior do que o número secreto.")
        else:
            print("Parabéns! Você acertou o número secreto em", tentativas, "tentativas.")
            break

if __name__ == '__main__':
    main()
