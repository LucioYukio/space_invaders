arquivo= open('pessoas.dat', 'r', encoding='utf-8')
linha= arquivo.readline()
contf= 0
contm= 0
maiorIdade= 0
while linha:
    linha= linha.strip()
    nome,sexo,idade = linha.split(';')
    print(linha)
    print(nome)
    print(sexo)
    print(idade)
    if sexo == 'F':
        contf= contf + 1
    else:
        contm= contm + 1
    if int (idade) > maiorIdade:
        maiorIdade= int(idade)

    linha= arquivo.readline()
arquivo.close()
print('Total de mulheres:', contf)
print('Total de homens: ', contm)
print('A maior idade entre as pessoas é:', maiorIdade)