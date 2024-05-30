cadena = input("Ingrese una cadena: ")

cadena_limpia = ""
for c in cadena:
    if c.isalnum():
        cadena_limpia += c.lower()

es_palindromo = True
n = len(cadena_limpia)
for i in range(n // 2):
    if cadena_limpia[i] != cadena_limpia[n - i - 1]:
        es_palindromo = False
        break


if es_palindromo:
    print("La cadena ingresada es palindroma")
else:
    print("La cadena ingresada no es palindroma")