numero= input("Digite um número para a tabuada:")
for i in range(1,11):
    print(numero + "x" + str(i) + "=" + str(i*int(numero)))
    # Devo converter o i para string, pois o print só trabalha com string
