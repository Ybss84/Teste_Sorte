import random

#Aonde ira solicitar os números
num1 = int(input("Informe o primeiro número de 01 a 60: "))
num2 = int(input("Informe o segundo número de 01 a 60: "))
num3 = int(input("Informe o terceiro número de 01 a 60: "))
num4 = int(input("Informe o quarto número de 01 a 60: "))
num5 = int(input("Informe o quinto número de 01 a 60: "))
num6 = int(input("Informe o sexto número de 01 a 60: "))

print("Os números escolhidos foi: {} {} {} {} {} {}".format(num1,num2,num3,num4,num5,num6))

#Aonde vai gerar os números de forma automática
numero1 = random.randrange(1, 60)
numero2 = random.randrange(1, 60)
numero3 = random.randrange(1, 60)
numero4 = random.randrange(1, 60)
numero5 = random.randrange(1, 60)
numero6 = random.randrange(1, 60)
print("Os números sorteados foi: {} {} {} {} {} {}".format(numero1,numero2,numero3,numero4,numero5,numero6))

#Informe se a pessoa acertou todos os número ou não
if num1 == numero1:
    print("Você acertou apenas um número")
elif num1 == numero1 or num2 == numero2:
    print("Você acertou apenas dois números")
elif num1 == numero1 or num2 == numero2 or num3 == numero3:
    print("Você acertou apenas três números")
elif num1 == numero1 or num2 == numero2 or num3 == numero3 or num4 == numero4:
    print("Você acertou apenas quatro números")
elif num1 == numero1 or num2 == numero2 or num3 == numero3 or num4 == numero4 or num5 == numero5:
    print("Você acertou apenas cinco números")
elif num1 == numero1 or num2 == numero2 or num3 == numero3 or num4 == numero4 or num5 == numero5 or num6 == numero6:
    print("Você acertou todos os números, parabéns e apresente o comprovante na loterica")
else:
    print("Você não acertou nenhum número, tente novamente ou depois")
