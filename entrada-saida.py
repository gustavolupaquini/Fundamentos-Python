nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")


idade = int(input("Insira sua idade: "))


if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.

nome = "Juan"
idade = 25


print(f"Olá, meu nome é {nome} e tenho {idade} anos.")