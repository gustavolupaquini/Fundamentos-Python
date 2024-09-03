def Mult(a, b):
    return a * b

resultado = Mult(5, 3)

print(resultado)

def Saudacao(nome):
    print(f"Olá, {nome}!")

Saudacao("Gustavo")

quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25

def Media(*numeros):
    soma = sum(numeros)
    qtd = len(numeros)
    media = soma / qtd 
    return media

print(Media(10, 20, 30, 40))



#Variaveis globais e locais


def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


#funcao()  # Imprime 10
#funcao2()  # Imprime 20
#print(variavel_global)  # Imprime 20
#print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.




#Documentando Funcoes



def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura


