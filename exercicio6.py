palavra = str(input("Digite uma palavra: ")).lower().strip()
verifica_palindromo = palavra[::-1]


if palavra == verifica_palindromo:
    print(f"A palavra {verifica_palindromo} é um palíndromo")

else:
    print(f"A palavra {verifica_palindromo} não é um palíndromo")