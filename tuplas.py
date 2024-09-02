#Tuplas
ponto = (3, 4) #Diferente das listas aqui usamos () e nao [], as tuplas sao imutaveis.

#print(ponto[0])  
#print(ponto[1])

#Métodos para tuplas
minha_tupla = (1, 2, 3, 2, 4, 2)

print (len(minha_tupla))   # Saída: 6

print (minha_tupla.index(3, 2, 4))   # Saída: 2 (Valor, inicio , fim) procura o indice do valor que especifquei no Range que defini (2, 4)

print (minha_tupla.index(2, 2))   # Saída: 3 (Valor, inicio) procura o indice do valor que especifquei apartir do inicio que especifiquei (2)

print (minha_tupla.index(2)) # Saída : 1 (Valor) retorna o indice da primeira ocorrencia do valor que especifiquei

print (minha_tupla.count(2)) # Saída: 3 Retorna quantas vezes o valor é presente na tupla



