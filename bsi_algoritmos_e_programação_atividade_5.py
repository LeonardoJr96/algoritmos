# -*- coding: utf-8 -*-
"""BSI- Algoritmos e programação- atividade 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hxEVpqcsXC3TsJk2S8bxTpV8PlHlFM6r
"""

2#
numero = float(input("digite um número: "))

if numero > 0:
  print("é positivo")
else:
  if numero == 0:
    print("é zero")
  else:
    print("é negativo")

3#
numero = float(input("digite um valor: "))

if numero > 10:
  print("É maior que 10!")
else:
  print('É menor que 10!')

4#
numero_1 = float(input("digite um número para soma: "))
numero_2 = float(input("digite outro número para soma: "))

soma = numero_1 + numero_2

if soma > 10:
  print(soma)
else:
  print("reiniciar programa")

5#
numero = float(input("digite um número: "))

divisao = numero % 5

if divisao == 0:
  ("ele é divisivio por 5")
else:
  ("não é divisivio por 5")

6#
numero = float(input("digite um número: "))

if numero < 90 and numero > 20:
  print(f'o número {numero} está entre 20 e 90')
else:
  print("o número não está entre 20 e 90")

7#
idade = int(input("escreva o ano de nascimento: "))
ano_atual = int(input("escreva o ano atual: "))

soma = ano_atual - idade

if soma >= 18:
  print("pode votar")
else:
  print("não pode votar")

8#
idade = int(input("escreva o ano de nascimento: "))
ano_atual = int(input("escreva o ano atual: "))

idade_real = ano_atual - idade

if idade_real >= 0:
  print(f'a idade é {idade_real}')
else:
  str(input("o ano está correto? "))

9#
idade = int(input("digite a sua idade: "))

if idade >= 65:
  print("65 anos ou mais")
else:
  if idade >= 18 and idade < 65:
    print("maior de idade")
  else:
    print("menor de idade")

10#
nota_1 = float(input("digite a nota da 1° avaliação: "))
nota_2 = float(input("digite a nota da 2° avaliação: "))

media = (nota_1 + nota_2) / 2

if media >= 6:
  print(f"aprovado, média {media}")
else:
  print(f"não aprovado, média {media}")

11#
nota_1 = float(input("digite a 1° nota: "))
nota_2 = float(input("digite a 2° nota: "))

media = (nota_1 + nota_2) / 2

if media >= 7:
  print("aprovado")
else:
  exame = float(input(f"sua média é {media} média inferior a 7,0, informe anota do exame: "))
  if exame >= 7:
    print("aprovado")
  else:
    print("reprovado")

12#
prof_1 = int(input("digite o número de horas aula do professor 1: "))
prof_2 = int(input("digite o número de horas aula do professor 2: "))
valor_1 = float(input("digite o valor recebido por hora do professor 1: "))
valor_2 = float(input("digite o valor por hora do professor 2: "))

resultado_1 = prof_1 * valor_1
resultado_2 = prof_2 * valor_2

if resultado_1 > resultado_2:
  print(f'o professor 1 recebe {resultado_1} e recebe mais que o professor 2 ({resultado_2})')
else:
  print(f'o professor 1 recebe {resultado_2} e recebe mais que o professor 2 ({resultado_1})')

13#
numero = int(input("digite um numero inteiro: "))

resultado = numero % 2

if resultado == 0:
  print("é par")
if resultado == 1:
  print("é impar")

14#
time_1 = str(input("escreva o nome do primeiro time: "))
time_2 = str(input("escreva o nome do outro time: "))
gols_1 = int(input("digite o nº de gols feitos do primeiro time: "))
gols_2 = int(input("digite o nº de gols do outro time: "))

if gols_1 > gols_2:
  print(f'{time_1} é o vencedor')
else:
  if gols_1 < gols_2:
    print(f'{time_2} é o vencedor')
  else:
    print("empate")

15#
sigla = str(input("digite a sigla do estado onde mora: "))

if sigla == 'RJ' or 'rj':
  print("Carioca")
else:
    if sigla == 'SP' or 'sp':
        print("Paulista")
    if sigla == "MG" or 'mg':
        print("Mineiro")
    else:
        print("Outros")

16#
produto = float(input("informe o valor do produto: "))
compras = int(input("quantos produtos comprou"))

valor_real = produto * compras

if compras == 1 and produto == 20 or 20.0:
  produto_1 = produto + (produto * 0.45)
  print(f'o valor do produto é R$ {produto}, o total, Lucro do comerciante de 45%, fica R$ {produto_1}')
else:
  if valor_real < 20:
    imposto = produto * 0.45
    valor_total = valor_real + imposto
    print(f'o valor do produto é R$ {produto}, o total, Lucro do comerciante de 45%, fica R$ {valor_total}')
  if valor_real > 20 or 20.0:
    imposto = produto * 0.30
    valor_total = valor_real + imposto
    print(f'o valor do produto é R$ {produto}, o total, Lucro do comerciante de 45%, fica R$ {valor_total}')

17# calendário mais completo, pois ja tinha feito algo parecido
dia = int(input('digite o dia que nasceu: '))
mes = str(input('escreva o mês em que nasceu: '))
ano = int(input('esreva o ano em que nasceu: '))
        
if mes == 'janeiro' or mes == '1' or mes == '01':
    mes_1 = 1
    print(f'vc nasceu {dia} de janeiro de {ano}, {dia}/{mes_1}/{ano}')
else:
    if mes == 'fevereiro' or mes == '2' or mes == '02':
        mes_1 = 2
        print(f'vc nasceu {dia} de fevereiro de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'março' or mes == '3' or mes == '03':
        mes_1 = 3
        print(f'vc nasceu {dia} de março de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'abril' or mes == '4' or mes == '04':
        mes_1 = 4
        print(f'vc nasceu {dia} de abril de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'maio' or mes == '5' or mes == '05':
        mes_1 = 5
        print(f'vc nasceu {dia} de maio de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'junho' or mes == '6' or mes == '06':
        mes_1 = 6
        print(f'vc nasceu {dia} de junho de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'julho' or mes == '7' or mes == '07':
        mes_1 = 7
        print(f'vc nasceu {dia} de julho de {ano}, {dia}/{mes_1}/{ano}')    
    if mes == 'agosto' or mes == '8' or mes == '08':
        mes_1 = 8
        print(f'vc nasceu {dia} de agosto de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'setembro' or mes == '9' or mes == '09':
        mes_1 = 9
        print(f'vc nasceu {dia} de setembro de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'outubro' or mes == '10':
        mes_1 = 10
        print(f'vc nasceu {dia} de outubro de {ano}, {dia}/{mes_1}/{ano}')
    if mes == 'novembro' or mes == '11':
        mes_1 = 11
        print(f'vc nasceu {dia} de novembro de {ano}, {dia}/{mes_1}/{ano}')
    else:
        mes_1 = 12 
        print(f'vc nasceu {dia} de dezembro de {ano}, {dia}/{mes_1}/{ano}')

18#
letra = str(input("digite uma letra: "))

if letra == 'A' or letra == 'a' or letra == 'E' or letra == 'e' or letra == 'I' or letra == 'i' or letra == 'O' or letra == 'o' or letra == 'U' or letra == 'u':
  print("é uma vogal")
else:
  print("é uma consoante")

19#
numero_1 = int(input("digite um número: "))
numero_2 = int(input(f'digite outro número diferente de {numero_1}: '))

if numero_2 == numero_1:
  numero_2 = int(input(f'digite um número diferente de {numero_1}: '))
  if numero_1 > numero_2:
    print(f'o número {numero_1} é maior!')
  else:
    print(f'o número {numero_2} é maior!')
else:
  if numero_1 > numero_2:
    print(f'o número {numero_1} é maior!')
  else:
    print(f'o número {numero_2} é maior!')

20#
numero_1 = int(input("digite um número: "))
numero_2 = int(input(f'digite outro número diferente de {numero_1}: '))

if numero_2 == numero_1:
  numero_2 = int(input(f'digite um número diferente de {numero_1}: '))
  if numero_1 > numero_2:
    print(numero_2, numero_1)
  else:
    print(numero_1, numero_2)
else:
  if numero_1 > numero_2:
    print(numero_2, numero_1)
  else:
    print(numero_1, numero_2)

21#
numero_1 = int(input("digite um número para A: "))
numero_2 = int(input(f'digite outro número diferente de {numero_1} para B: '))
numero_3 = int(input(f'digite outro número diferente de {numero_1} e {numero_2} para C: '))

if numero_2 == numero_1 or numero_2 == numero_3:
  numero_2 = int(input(f'digite um número diferente de {numero_1} e {numero_3} para B: '))
if numero_3 == numero_1:
    numero_3 = int(input(f'digite um número diferente de {numero_1} e {numero_2} para C : '))
    if numero_1 > numero_2 and numero_1 > numero_3:
      print(numero_1)
    if numero_2 > numero_3 and numero_2 > numero_1:
      print(numero_2)
    if numero_3 > numero_1 and numero_3 > numero_2:
      print(numero_3)
else:
  if numero_1 > numero_2 and numero_1 > numero_3:
    print(numero_1)
  if numero_2 > numero_3 and numero_2 > numero_1:
    print(numero_2)
  if numero_3 > numero_1 and numero_3 > numero_2:
    print(numero_3)

22#
numero_1 = int(input("digite um número para A: "))
numero_2 = int(input(f'digite outro número diferente de {numero_1} para B: '))
numero_3 = int(input(f'digite outro número diferente de {numero_1} e {numero_2} para C: '))

if numero_2 == numero_1 or numero_2 == numero_3:
  numero_2 = int(input(f'digite um número diferente de {numero_1} e {numero_3} para B: '))
if numero_3 == numero_1:
    numero_3 = int(input(f'digite um número diferente de {numero_1} e {numero_2} para C : '))
    if numero_1 > numero_2 > numero_3:
      print(numero_1 + numero_2)
    if numero_1 > numero_3 > numero_2:
      print(numero_1 + numero_3)
    if numero_2 > numero_1 > numero_3:
      print(numero_1 + numero_2)
    if numero_2 > numero_3 > numero_1:
      print(numero_3 + numero_2)
    if numero_3 > numero_1 > numero_2:
      print(numero_1 + numero_3)
    if numero_3 > numero_2 > numero_1:
      print(numero_3 + numero_2)
else:
  if numero_1 > numero_2 > numero_3:
    print(numero_1 + numero_2)
  if numero_1 > numero_3 > numero_2:
    print(numero_1 + numero_3)
  if numero_2 > numero_1 > numero_3:
    print(numero_1 + numero_2)
  if numero_2 > numero_3 > numero_1:
    print(numero_3 + numero_2)
  if numero_3 > numero_1 > numero_2:
    print(numero_1 + numero_3)
  if numero_3 > numero_2 > numero_1:
    print(numero_3 + numero_2)

23#
numero_1 = int(input("digite um número para A: "))
numero_2 = int(input(f'digite outro número diferente de {numero_1} para B: '))
numero_3 = int(input(f'digite outro número diferente de {numero_1} e {numero_2} para C: '))

if numero_2 == numero_1 or numero_2 == numero_3:
  numero_2 = int(input(f'digite um número diferente de {numero_1} e {numero_3} para B: '))
if numero_3 == numero_1:
    numero_3 = int(input(f'digite um número diferente de {numero_1} e {numero_2} para C : '))
    if numero_1 > numero_2 > numero_3:
      print(numero_1, numero_2, numero_3)
    if numero_1 > numero_3 > numero_2:
      print(numero_1, numero_3, numero_2)
    if numero_2 > numero_1 > numero_3:
      print(numero_2, numero_1, numero_3)
    if numero_2 > numero_3 > numero_1:
      print(numero_2, numero_3, numero_1)
    if numero_3 > numero_1 > numero_2:
      print(numero_3, numero_1, numero_2)
    if numero_3 > numero_2 > numero_1:
      print(numero_3, numero_2, numero_1)
else:
  if numero_1 > numero_2 > numero_3:
    print(numero_1, numero_2, numero_3)
  if numero_1 > numero_3 > numero_2:
    print(numero_1, numero_3, numero_2)
  if numero_2 > numero_1 > numero_3:
    print(numero_2, numero_1, numero_3)
  if numero_2 > numero_3 > numero_1:
    print(numero_2, numero_3, numero_1)
  if numero_3 > numero_1 > numero_2:
    print(numero_3, numero_1, numero_2)
  if numero_3 > numero_2 > numero_1:
    print(numero_3, numero_2, numero_1)

24#
nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("digite a segunda nota: "))

media = (nota_1 + nota_2) / 2

if media <= 3.9:
  print("nota E")
else:
  if media >= 4 and media <= 5.9:
    print("nota D")
  if media >= 6 and media <= 7.49:
    print("nota C")
  if media >= 7.5 and media <= 8.9:
    print("nota B")
  if media >=9 and media <= 10:
    print("nota A")

25#
# inicial

numero_1 = float(input("digite um número: "))
sinal = str(input("digite o sinal: "))
numero_2 = float(input("digite outro número: "))

# condições

#somar
if sinal == '+':
    resultado = numero_1 + numero_2
else:
 
#subtrair
    if sinal == '-':
        resultado = numero_1 - numero_2

#multiplicar
    if sinal == '*' and 'x':
        resultado = numero_1 * numero_2

#dividir
    if sinal == '/':
        resultado = numero_1 / numero_2

# resultado
(print(resultado))

26#
import math
a = float(input("digite um valor para A: "))
b = float(input("digite um valor para B: "))
c = float(input("digite um valor para C: "))

basca = (b ** 2) - 4 * a * c
basca2 = math.sqrt(basca)
basca_1 = ((- b) + basca2) / 2 * a
basca_2 = ((- b) - basca2) / 2 * a

if basca > 0:
  print(f"a dois resultados, X1 = {basca_1}, X2 = {basca_2}")
else:
  if basca == 0:
    print(f'a apenas um resultado, X = {basca_1}')
  if basca < 0:
    print("não há resultados")

27#
a = int(input("digite um valor para A: "))
b = int(input("digite um valor para B: "))
c = int(input("digite um valor para C: "))

triangulo = str(input("é um triangulo? sim ou não: "))

if triangulo == 'sim' or triangulo == 'Sim':
  if a == b and b == c:
    print("é um triângulo equilátero")
  else:
    if a == b or a == c:
      print("é isósceles")
    if b == c:
      print("é isóceles")
    else:
      print("é escaleno")
else:
  print("os valores lidos não formam um triângulo")

28#
a = float(input("digite um número para A: "))
b = float(input("digite um número para B: "))
c = float(input("digite um número para C: "))
opcao = int(input("escolhe uma  número de 1 a 3: "))

if a <= 0 or b <= 0 or c <= 0 or opcao <= 0:
  print("reinicie o programa!")
else:
  if opcao == 2:
    if a > b > c:
      print(a, b, c)
    else:
      if a > c > b:
        print(a, c, b)
      if b > a > c:
        print(b, a, c)
      if b > c > a:
        print(b, c, a)
      if c > a > b:
        print(c, a, b)
      if c > b > a:
        print(c, b, a)
  if opcao == 1:
    if a > b > c:
      print(c, b, a)
    else:
      if a > c > b:
        print(b, c, a)
      if b > a > c:
        print(c, a, b)
      if b > c > a:
        print(a, c, b)
      if c > a > b:
        print(b, a, c)
      if c > b > a:
        print(a, b, c)
  if opcao == 3:
    if a > b > c:
      print(b, a, c)
    else:
      if a > c > b:
        print(c, a, b)
      if b > a > c:
        print(a, b, c)
      if b > c > a:
        print(c, b, a)
      if c > a > b:
        print(a, c, b)
      if c > b > a:
        print(a, c, a)

29#
salario = float(input("digite o seu salário: "))

if salario <= 400.0:
  aumento = salario * 0.15
  salario_real = salario + aumento
else:
  if salario > 400.0 and salario <= 700.0:
    aumento = salario * 0.12
    salario_real = salario + aumento
  if salario > 700 and salario <= 1000:
    aumento = salario * 0.10
    salario_real = salario + aumento
  if salario > 1000 and salario <= 1500:
    aumento = salario * 0.07
    salario_real = salario + aumento
  if salario > 1500 and salario <= 2000:
    aumento = salario * 0.04
    salario_real = salario + aumento
  if salario > 2000:
    aumento = salario * 0
    salario_real = salario + aumento
print(f'o seu salário é R$ {salario}, o novo salário corrigido é R$ {salario_real}')

30#
salario = float(input("digite o seu salário: "))

if salario < 10000:
  aumento = salario * 0.55
  salario_real = salario + aumento
else:
  if salario >= 10000 and salario <= 25000:
    aumento = salario * 0.20
    salario_real = salario + aumento
  if salario > 25000:
    aumento = salario * 0.20
    salario_real = salario + aumento
print(f'o novo salário a receber é R$ {salario_real}')

31#
temperatura = int(input("digite quantos graus o forno irá operar: "))

if temperatura <= 500:
  print("temperatura inválida")
else:
  if 500 < temperatura and temperatura < 700:
    print("aquecimento ligado em 100%")
  if 700 <= temperatura and temperatura < 735:
    print("aquecimento ligado em 50%")
  if 735 <= temperatura and temperatura < 780:
    print("aquecimento desligado")
  if 780 <= temperatura and temperatura <= 1000:
    print("superaquecidos")

32#
valor = int(input("digite um número de 1 a 4: "))
numero1 = float(input("digite um número: "))
numero2 = float(input("digite outro número: "))

if valor == 0:
  resultado = numero1 + numero2
  print(resultado)
else:
  if valor == 1:
    resultado = numero1 - numero2
    print(resultado)
  if valor == 2:
    resultado = numero1 * numero2
    print(resultado)
  if valor == 3:
    resultado = numero1 / numero2
    print(resultado)
  if valor == 4:
    resultado = (numero1 + numero2) / 2
    print(resultado)
  if valor < 0 and valor >= 5:
    print('Valor errado. Programa encerrando sem cálculos')

33#
a = int(input("escreva um número: "))
b = int(input("escreva outro número: "))

divisao = a % b
resto = a / b
par_impar_a = a % 2
par_impar_b = b % 2

if divisao == 1:
    soma = a + b
    print(F'a soma é{soma} e o resto é {divisao}')
if divisao == 2:
    if par_impar_a == 1 and par_impar_b == 1:
        print("impar")
        print("impar")
    if par_impar_a == 0 and par_impar_b == 0:
        print("par")
        print("par")
    if par_impar_a == 1 and par_impar_b == 0:
        print("impar")
        print("par")
    if par_impar_a == 0 and par_impar_b == 1:
        print("par")
        print("impar")
if divisao == 3:
    resultado = (a + b) * a
    print(resultado)
if divisao == 4:
    resultado = (a + b) / b
    print(resultado)
else:
    if divisao < 0 or divisao > 4:
        resultado (a + b) ** 2
        print(resultado)

34#
a = int(input("digite a idade do homem A: "))
b = int(input("digite a idade do homem B: "))
c = int(input("digite a idade do mulher A: "))
d = int(input("digite a idade do mulher B: "))

if a > b and c > d:
  resultado_2 = a + c
  resultado_1 = b * d
else:
  if a > b and c < d:
    resultado_2 = a + c
    resultado_1 = b * c
  if a < b and c > d:
    resultado_2 = b + c
    resultado_1 = a * d
  if a < b and c < d:
    resultado_2 = b + d
    resultado_1 = a * c     

print(f'a soma do homem mais velho com a mulher mais velha é {resultado_2}')
print(f'o produto do homem mais novo com a mulher mais nova é {resultado_1}')





















