# -*- coding: utf-8 -*-
"""BSI- Algoritmos e programação- atividade 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZlU_Ifozug6TdLSWsiBq8c3ghuxkFC6F
"""

lad = float(input("digite o lado do quadrado: "))
area = lad ** 2
peri = lad * 4

print("a area do quadrado é", area, "e o comprimento é", peri)

nome = str(input("digite o nome da pessoa: "))
fil = int(input("digite a quantidade de filhos: "))
print(nome, "tem", fil, "filhos")

alt = float(input("digite a altura do retângulo: "))
base = float(input("digite a base do retângulo: "))

area = float(base * alt)
peri = float(2 * (base + alt))

print("o perímetro do retângulo é", peri, "e a area", area)

lad = float(input("digite o lado do cubo: "))

area = float(6 * (lad ** 2))
vol = lad **3

print("a area é", area)
print("o volume é", vol)

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

quo = int(num1 // num2)
rest = int(num1 % num2)

print("o quociente é:", quo)
print("o resto é:", rest)

base = float(input("digite a base: "))
alt = float(input("digite a altura: "))

area = (base * alt) / 2

print("a área é:", area)

import math

raio = float(input("digite o raio: "))

perimetro = 2 * math.pi * raio
area = math.pi * (raio ** 2)

print("o perímetro é:", perimetro)
print("a área é:", area)


print("fim")