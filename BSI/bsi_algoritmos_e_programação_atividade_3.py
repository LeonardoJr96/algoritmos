# -*- coding: utf-8 -*-
"""BSI- Algoritmos e programação- atividade 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yTE3j2jBaxfkzTJfKIInXB1l_oHrfN_2
"""

1#
print("Alo mundo")

2#
num = str(input("digite um número: "))
print("O número informado é", num)

3#
num1 = float(input("digite 1° número: "))
num2 = float(input("digite o 2° número: "))
soma = int(num1 + num2)
print(soma)

4#
print("digite as suas notas bimestrais")
not1 = float(input("nota 1: "))
not2 = float(input("nota 2: "))
not3 = float(input("nota 3: "))
not4 = float(input("nota 4: "))
med = (not1 + not2 + not3 + not4)/4
print("sua média é", med)

5#
cem = float(input("digite o tamanho em metros para a conversão: "))
convert = float(cem * 100)
print("A conversão de", cem, "m para centimetros é", convert, "cm")

6#
import math
rai = int(input("digite o número do raio: "))
A = int(math.pi * (rai ** 2))
print("A área do quadrado é", A)

7#
lad = float(input("digite o lado: "))
quad = lad ** 2
quad2 = quad * 2
print(int(quad))
print(int(quad2))

8#
hora = float(input("quanto você ganha por hora? "))
mes = float(input("quantas horas você trabalha por dia? "))
res = hora * mes
print("Você ganha por mês R$",res)

9#
fah = int(input("digite os graus farenheit: "))
C = int(5 * (fah - 32) / 9)
print(C)

10#
cel = int(input("digite os graus farenheit: "))
F = int(((9 * cel)/5) + 32)
print(F)

11# float =número real
int1 = int(input("ditige um número sem casa decimal: "))
int2 = int(input("digite outro número sem casa decimal: "))
real1 = float(input("digite um número com casa decimal"))

A = (2 * int1) * (int2 / 2)
B = (int1 * 3) + real1
C = real1 ** 3

print(A)
print(B)
print(C)

12#
alt = float(input("digite a sua altura: "))
peso = (72.7 * alt) - 58
print("seu peso é", peso)

13#
sexo = str(input("digite o seu sexo (masculino ou feminino): "))
altura = float(input("digite a sua altura: "))

if sexo == "masculino":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7
print(f'seu peso ideal seria {peso_ideal} kg')

peso = float(input("informe seu peso: "))

if peso == peso_ideal:
    print("seu peso está dentro")
else:
    if peso < peso_ideal:
        print("você está abaixo do peso ideal")
    else:
        print("você está acima do peso ideal")

14#
peso = int(input("informe quantos kg de peixe pesecou: "))

if peso <= 50:
    excesso = 0
    multa = excesso * 4
    print("não há excessos e nem multa")
else:
    excesso = peso % 50
    multa = excesso * 4
    print(f'o valor a pagar dos {excesso} kg de peixe é de R${multa}')

15#
hora = float(input("Quanto você ganha por hora: "))
mes = float(input("quantas horas vc trabalha por mês: "))

rend_total = mes * hora
imposto = rend_total * 0.11
inss = rend_total * 0.08
sind = rend_total * 0.05
rend_liquid = rend_total - (imposto + inss + sind)

print("+ Salário Bruto : R$", rend_total)
print("- IR (11%) : R$", imposto)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sind)
print("= Salário liquido : R$", rend_liquid)

16#
import math

tamanho = float(input("Quantos metros quadrados irá pintar? "))

lata = float(tamanho / 3)
lata1 = math.ceil(lata / 18) 
preco = int(lata1 * 80)

print("será necessária", lata1,"latas e custará no total : R$", preco)

17#
import math

tamanho = float(input("Quantos metros quadrados irá pintar? "))

#simples

parede = (math.ceil(tamanho / 6) * 1.1)
lata = math.ceil(parede / 18)
galao = math.ceil(parede / 3.6)
preco_lata = int(80 * lata)
preco_galao = int(25 * galao)

#misturado

lao = math.floor(parede / 18)
lao1 = parede % 18
lao2 = math.ceil(lao1/3.6)
preco_lao = lao * 80
preco_lao2 = lao2 * 25
preco_total = preco_lao + preco_lao2


#imagem
print("será necessário", lata,"latas de 18 litros por: R$", preco_lata)
print("Será necessário", galao,"galões de 3,6 litros por: R$", preco_galao)
print("será necessários",lao1, "galões e", lao2, "latas por: R$", preco_total)

18#
arquivo = float(input("digite o tamanho de memória, em MB: "))
velocidade = float(input("digite a velocidade da internet, em Mbps: "))

vel = (velocidade / 8)
tempo = float((arquivo / vel) / 60)

print("O tempo aproximado:", tempo, "min")