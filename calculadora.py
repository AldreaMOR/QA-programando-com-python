valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))

print("A soma dos valores é",(valor1 + valor2))
print("A subtração dos valores é",(valor1 - valor2))
print("A multiplicação dos valores é",(valor1 * valor2))

if (valor2 == 0):
    print("Não é possível realizar divisão por zero")
else:
    print("A divisão dos valores é",(valor1 / valor2))