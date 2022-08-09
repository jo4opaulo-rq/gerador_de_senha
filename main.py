from gerarsenha import Senha

while True:
    tam = int(input("Informe a quantidade de caracteres para a senha: "))
    if tam > 5:
        Senha(tam)
        break
    else:
        print("\n     Senha muito pequena, informe um valor maior que 5\n")