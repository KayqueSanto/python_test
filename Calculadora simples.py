import sys

limite_caracter = 10

nome = input("Digite seu nome: ")

if len(nome) > limite_caracter:
    print("O nome inserido excede o limite de caracteres permitido.")
    sys.exit()  # Isso interromperá o programa
else:
    print("Olá:", nome)

num1 = float(input("Digite um valor: "))
operacao = input("Escolha a operação matemática: *, +, -, /")
num2 = float(input("Digite outro valor: "))

if operacao == "*":
    resultado = num1 * num2
    print("O resultado é:", resultado)

elif operacao == "+":
    resultado = num1 + num2
    print("O resultado é:", resultado)
    
elif operacao == "-":
    resultado = num1 - num2
    print("O resultado é:", resultado)
    
elif operacao == "/":
    resultado = num1 / num2
    print("O resultado é:", resultado)
    
else: 
    print("Operação inválida")
