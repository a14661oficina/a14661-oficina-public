print ("Hello World")
ValorA = float(input("Insira um valor entre 1 - 20: "))
ValorB = float(input("Insira um valor entre 1 - 20: "))
Soma = ValorA + ValorB
print(Soma)
media = Soma + Soma *2
print(media) 


#EX 0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("insira a sua idade: ")
nome = input("insira o seu nome: ")
print(f"O meu nome é {nome} e tenho {idade} anos. ");


#EX 0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("ola mundo!" )
fruta = "banana"
print(f"EU gosto de {fruta}" )


#EXO.3
"""Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
Nome = input("insira o nome: ")
print (f"Boas mano, {Nome}, tem um grande dia!: ")
valor = int(input("Insira um numero:"))
dobro = valor * 2 
print  (f" o dobro de {valor} é {dobro}")


#EX1.1
"""Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco"""
A=("\n Bem-vindos ao Phynton! ")
print(A) 

#EX1.2
"""Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco"""
A=("\n Martim, bem-vindo ao Phyton:")
print(A)

#EX1.3
"""Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável."""
print("Ola tudo bem?")
valor=input("Qual é o teu nome?") 
print(f"\nBom dia {valor}. ")

#EX1.4
"""Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis."""
nome= "Martim Brandao" 
idade= int("15") 
localidade= "Sao martinho"
print(f"{nome} tem {idade} anos e vive em {localidade}")

#EX1.5
"""Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem"""
linguagemProg= "Phyton"
Nome="Martim Brandao"
print(f"O {Nome} sabe formatar no {linguagemProg}")

#EX1.6
"""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."""
print(f"{'Bem-vindo ao Phyton':<20}")
print(f"{'Bem-vindo ao Phyton':>50}")
print(f"{'Bem-vindo ao Phyton':^310}")


#EX1.7
"""Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.""" 
raio=float(input(" Insire o valor do raio: "))
perimetro = 2  * 3,14 * raio
print(f"O perimetro é: {perimetro}")
area = 3,24 * raio * raio
print(f"A area é: {area}")


#EX1.8
"""Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20"""
import datetime
x = datetime.datetime.now()
dia  = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%y")
hora = x.strftime("%H")
minutos = x.strftime("%M")
segundos = x.strftime("%S")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}-{minutos}-{segundos}")


#EX1.9
"""Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos."""
numero=input("Insira um numero: ")
pontos=input("Insira a pontuação final: ")
print(f"O atleta {numero} teve {pontos} pontos. ")

#EX1.10
"""Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual."""


import datetime
birthdate = input("Insire a data do seu nascimento: ")
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print("Atua idade é",age,"anos.")

#EX1.11
"""Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO)."""
libras = float(input("Quantas libras?: "))
euro = libras * 1.19
print(f"O valor em euros é: {euro}")


idade = int(input("Qual é a sua idade: "))
if idade < 12:
  print("Voce é uma criança!")
elif idade < 18: 
      print("Voce é um adolescetne")
elif idade < 25:
        print("voce é um adulto")


import random 

segredo = int(random.randint(0, 5))
print(f"o numero secreto é: {segredo}")


numeroescolhido = int(input("insire um valor enrte (0 e 5):"))

if numeroescolhido > segredo:
   print("O numero inserido é maior de que o meu!")  
elif numeroescolhido < segredo: 
  print("O numeor escolhido é menor do que o meu!")
print("Acertaste!")


velocidade = int(input("Qual a velociade do carro em km : "))
if velocidade>80:
  print("Voce foi multado")
multa = velocidade - 80 
preço  = multa * 7 
print(f"A sua multa foi {preço} €")


#Exercício FP1: Verificar se um número é positivo, negativo ou zero.
"""Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else."""

numero = int(input("Insire um numero: ")) 
if numero > 0: 
  print("Numero positivo.")
elif numero < 0:
  print("Numero negativo.")
else: 
  print("Numero é igual a zero.")


  
  #Exercício FP2: Verificar se um número é par ou ímpar.
  """Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
  Dica: Para verificar se um número é par, utilize a operação de módulo %."""

  numero = int(input("Insire um numero: "))
  if numero % 2 == 0:
    print("O numero é par.")
  elif numero % 2 == 1:
    print("O numero é impar.")


#Exercício FP3: Calcular a nota final de um aluno.
"""Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"
"""

nota = int(input("Insire a sua nota: "))
if nota < 10: 
  print("Reprovado.")
elif nota >=10 and nota <= 14:
  print("Suficiente.")
elif nota >= 15 and nota <= 17:
  print("Bom.")
elif nota > 17:
  print("Muito bom.")


#Exercício FP4: Conversor de temperaturas.
"""Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15"""

Graus = float(input("Insire a temperatura em graus Celsius: "))
Fahrenheit =   Graus * 9/5 + 32
Kelvin = Graus + 273.15
unidade = input("Esolha a unidade do destino: ")
print(f"Os graus em Kelvin sao {Kelvin} e em Fahrenheit fica {Fahrenheit}.")




#Exercício FP5: Cálculo de impostos
"""Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto."""

salario = int(input("Insire o seu salario:"))
if salario < 1000: 
  print("isento de impostos.")
elif salario >= 1001 and salario <= 2000: 
  imposto = salario * 0.10%
  print(f"o imposoto é {imposto}.")
elif salario > 2000:
  imposto = salario * 0.20%
  print(f"O imposot é de {imposto}.")



#Exercício FP6: Imprimir números de 1 a 10.
"""Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10."""

for i in range(1,11):
  print(i)   



#Exercício FP7: Soma de números de 1 a 100.
"""Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

"""
soma = 0 
numero = 1 
while numero <= 100:
  soma += numero
  numero += 1 
print(f"A soma de 1 a 100 é {soma}.")




#Exercício FP8: Contagem de vogais numa string.
"""Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase."""

frase = (input("Qual o seu nome: "))
vogal = "a, e, i, o, u, A, E, I, O, U "
contador = 0 
for letra in frase:
  if letra in vogal:
    contador += 1
print(f"Numero de vogais: {contador}")


#Exercício FP9: Listar múltiplos de 5.
"""Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50."""

for i in range(5,51,5):
  print(i)



#Exercício FP10: Verificar se um número é primo.
"""Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.""""

numero = int(input("Insire um numero: "))
if numero % 2 == 0:
  print(f"O {numero} é primo.")
else:
  print(f"O numero não é primo.")


#Exercício FP12: Gerar uma lista de números pares.
"""Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista."""
lista = []
for i in range(1, 21):
  if i % 2 == 0:
    lista.append(i)
print(f"Lista de numeros pares: {lista}


 texto = str(input("Insire um texto: "))
      textoinv = texto [::-1]
      print (textoinv)


num = int(input("Insre um numero: "))
i = 1
  while i < 11:
   mult = num * i
   print(f"{num} x {i} = {mult}")
i += 1
