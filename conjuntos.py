frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}

intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3} RETORNA O VALOR QUE SE REPETE EM AMBOS CONJUNTOS

diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2} RETORNA OS VALORES QUE ESTAO NO CONJ1 MAS NAO NO CONJ2



diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}
"""
Os elementos 1 e 2 estão em conjunto1 mas não estão em conjunto2.
Os elementos 4 e 5 estão em conjunto2 mas não estão em conjunto1.
O elemento 3 está presente em ambos os conjuntos, portanto, não é incluído no resultado da diferença simétrica
"""



#Métodos de conjuntos
frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"} REMOVE O QUE FOI ESPECIFICADO, SE NAO EXISTIR NA LISTA NADA ACONTECE

frutas.clear()
print(frutas)  # Imprime set()