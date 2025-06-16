n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

# Operações matemáticas
print("------------Operações matemáticas------------")
soma = n1 + n2
print(f"A soma de {n1} e {n2} é: {soma}")
subtracao = n1 - n2
print(f"A subtração de {n1} menos {n2} é: {subtracao}")
multiplicacao = n1 * n2
print(f"A multiplicação de {n1} por {n2} é: {multiplicacao}")
if n2 != 0:
    divisao = n1 / n2
    print(f"A divisão de {n1} por {n2} é: {divisao:.0f}")
else:
    print("Não é possível dividir por zero.")
    
# Par ou Impar
print("------------Par ou Impar------------")
par = n1 % 2 
if par == 0:
    print ('O primeiro número digitado {} é PAR' .format(n1)) 
else:
    print ('O primeiro número digitado {} é ÍMPAR' .format(n1))

par = n2 % 2 
if par == 0:
    print ('O segundo número digitado {} é PAR' .format(n2)) 
else:
    print ('O segundo número digitado {} é ÍMPAR' .format(n2))
    
# Primo
print("------------Primero número digitado é primo?------------")
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print(end='')
        tot += 1
    else:
        print(end='')
    print('{} ' .format(c), end='')
print('\nO primeiro número digitado {} foi dividível {} vezes' .format(n1, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
    
print("------------Segundo número digitado é primo?------------")
tot = 0
for c in range(1, n2 + 1):
    if n2 % c == 0:
        print(end='')
        tot += 1
    else:
        print(end='')
    print('{} ' .format(c), end='')
print('\nO segundo número digitado {} foi dividível {} vezes' .format(n2, tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')