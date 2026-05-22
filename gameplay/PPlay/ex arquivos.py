arquivo = open('arquivos.dat', 'r')
linha = arquivo.readline ()
contdiv3 = 0
while linha:
    numero= int(linha)
    if numero %3 ==0:
        contdiv3= contdiv3 + 1
        print(numero)
    linha= arquivo.readline()
print('total de multiplos de 3= ', contdiv3)
arquivo.close()