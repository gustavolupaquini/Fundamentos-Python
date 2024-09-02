frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

#Printar do último da lista apartir (-1 ultimo) (-2 penultimo) ...
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

frutas = ["maçã", "banana", "laranja"]

#Adiciona um item no final da lista
frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

#Insere na posicao que voce especificar
frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

#Remove o item que voce explicitar
frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

#Remove e retorna o que foi retirado podendo assim armazena-lo em uma String
fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"

#Ordena os elementos da lista em ordem ascendente.
frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]

#Inverte a ordem dos elementos na lista.
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

#Lista de compreensão
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0] #x ** 2(Eleva cada numero (x) ao quadrado e x % 2 == 0 filtra os numeros pares)
print(quadrados)  # Imprime [4, 16]

