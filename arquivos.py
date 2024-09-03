#Leitura e escrita de arquivos
# leitura ("r"), escrita ("w") ou anexar ("a")

"""
arquivo = open("dados.txt", "w")
conteudo = arquivo.write("Teste")
arquivo.close()

arquivo = open("dados.txt" , "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    #Arquivo é fechado automaticamente

"""
 
