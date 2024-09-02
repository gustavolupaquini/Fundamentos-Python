#For0
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

for numero in range(1, 6):
    print(numero * 2)


#While
contador = 1

while contador < 5:

    print(contador * 2)
    contador += 1

#Break
contador = 0

while True:

    print(contador)
    contador += 1

    if contador == 5:
        break
    

#Continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
"""
Continue (Verificando se numeros sao pares)
Neste exemplo o continue só sera ser executado se o numero for divisivel por 2 ou seja um numero Par, que ira acionar o print
e printar o numero par na tela.
"""

#Pass
for i in range(5):
    pass
"""
Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.
"""