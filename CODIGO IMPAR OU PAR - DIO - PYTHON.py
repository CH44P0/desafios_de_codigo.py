#código que eu fiz!

## PARA O USUÁRIO INFORMAR UM NUMERO INTEIRO
numero = int(input("VALIDADOR DE PAR OU IMPAR \ndigite aqui um número inteiro:"))


#FUNÇÃO VALIDAR PAR IMPAR
def validar_par_impar (numero):
    if numero % 2 == 0:
        print(f"o número {numero} é par!")
    else:
        print(f"o numero {numero} é impar!")

validar_par_impar (numero)



#código que aceitaram!
## PARA O USUÁRIO INFORMAR UM NUMERO INTEIRO
numero = int(input())


#FUNÇÃO VALIDAR PAR IMPAR
def validar_par_impar (numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

validar_par_impar (numero)