"""
import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

#Funcao SQRT calcula a raiz quadrada de um valor

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

#Aqui importamos especificamente a funcao do modulo de maths
"""

"""
Math:
Fornece funções matemáticas, como sqrt() (raiz quadrada), sin() (seno), cos() (cosseno), entre outras.

Random:
Oferece funções para gerar números aleatórios, como random() (número aleatório entre 0 e 1), randint() (número inteiro aleatório em um intervalo), entre outras.

Datetime:
Permite trabalhar com datas e horas, como datetime.now() (data e hora atual), datetime.date() (data), datetime.time() (hora), entre outras.

"""

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

import meu_modulo


meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # Imprime 8