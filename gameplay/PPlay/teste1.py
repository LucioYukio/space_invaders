n = int(input())
alpha = 0
while alpha < n:
    alpha += 1
    cartas_mostradas = list(input().split())
    carta_base = cartas_mostradas[0]
    numero_da_minha = carta_base[0]
    nipe = carta_base[1]
    carta1 = cartas_mostradas[1]
    numero1 = carta1[0]
    if numero1 == "T":
        numero1 = 10
    if numero1 == "J":
        numero1 = 11
    if numero1 == "Q":
        numero1 = 12
    if numero1 == "K":
        numero1 = 13
    nipe1 = carta1[1]
    if nipe1 == "H":
        numero1 += 0.1
    if nipe1 == "C":
        numero1 += 0.2
    if nipe1 == "D":
        numero1 += 0.3
    if nipe1 == "S":
        numero1 += 0.4
    carta2 = cartas_mostradas[2]
    numero2 = carta2[0]
    if numero2 == "T":
        numero2 = 10
    if numero2 == "J":
        numero2 = 11
    if numero2 == "Q":
        numero2 = 12
    if numero2 == "K":
        numero2 = 13
    nipe2 = carta2[1]
    if nipe2 == "H":
        numero2 += 0.1
    if nipe2 == "C":
        numero2 += 0.2
    if nipe2 == "D":
        numero2 += 0.3
    if nipe2 == "S":
        numero2 += 0.4
    carta3 = cartas_mostradas[3]
    numero3 = carta3[0]
    if numero3 == "T":
        numero3 = 10
    if numero3 == "J":
        numero3 = 11
    if numero3 == "Q":
        numero3 = 12
    if numero3 == "K":
        numero3 = 13
    nipe3 = carta3[1]
    if nipe3 == "H":
        numero3 += 0.1
    if nipe3 == "C":
        numero3 += 0.2
    if nipe3 == "D":
        numero3 += 0.3
    if nipe3 == "S":
        numero3 += 0.4
    if numero1 < numero2 < numero3:
        saltos = 1
    if numero1 < numero3 < numero2:
        saltos = 2
    if numero2 < numero1 < numero3:
        saltos = 3
    if numero2 < numero3 < numero1:
        saltos = 4
    if numero3 < numero1 < numero2:
       saltos = 5
    if numero3 < numero2 < numero1:
        saltos = 6
    while saltos > 0:
        saltos = saltos - 1
        numero_da_minha += 1
        if numero_da_minha == 14:
            numero_da_minha = 1
    if numero_da_minha == 10:
        numero_da_minha = "T"
    if numero_da_minha == 11:
        numero_da_minha = "J"
    if numero_da_minha == 12:
        numero_da_minha = "Q"
    if numero_da_minha == 13:
        numero_da_minha = "K"
    minha_carta = numero_da_minha + nipe
    print(minha_carta)