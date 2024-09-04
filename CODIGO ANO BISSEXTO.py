#informar ano
ano = int(input())
#função validar ano bissexto
def verificador_ano_bissexto (ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("SIM")
    else:
        print("NÃO")

verificador_ano_bissexto(ano) 