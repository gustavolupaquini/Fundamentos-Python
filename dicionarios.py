#Dicionarios
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa["nome"])  # Imprime "João"
print(pessoa["idade"])    # Imprime 25
print(pessoa["cidade"])  # Imprime "Madri"

#O método get permite acessar os valores do dicionário de maneira mais segura, pois ele não gera um erro se a chave não existir; em vez disso, ele retorna None (ou um valor padrão especificado).
print(pessoa.get("nome"))   # Imprime "João"
print(pessoa.get("idade"))  # Imprime 25
print(pessoa.get("cidade")) # Imprime "Madri"

#Métodos de Dicionarios
pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])

pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}


