import random
from string import digits, punctuation, ascii_uppercase, ascii_lowercase
from time import strftime, localtime

tam = int(input("Informe a quantidade de caracteres para a senha: "))


def Senha(tamanho):
    simbolos = ascii_lowercase + digits + ascii_uppercase + punctuation
    simbolos_aleatorios = random.SystemRandom()
    senha = "".join(simbolos_aleatorios.choice(simbolos) for i in range(tamanho))
    horario = strftime('%d-%m-%y %H:%M:%S', localtime())

    arquivo = open('senhas.txt', 'a')
    print("-------------------------------------------", file=arquivo)
    print("Senha gerada no horário", horario, file=arquivo)
    print(senha, file=arquivo) 
    arquivo.close()
    print("Senha salva")


while tam <= 5: 
        tam = int(input("Informe a quantidade de caracteres para a senha: "))
    
Senha(tam)