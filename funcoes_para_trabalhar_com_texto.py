"""
    Ver todos comandos para string
    dir(str)
    
"""
print("Todas funções para string")
print(dir(str))

print("\n")

"""
    Strings se comportão como se uma lista
    Exemplo:
    nome = "Napoleão Kazu Onaya"
    nome[:9]

"""
print("Retorno da lista de uma string")
nome = "Napoleão Kazu Onaya"
print(nome[0:9])

print("\n")

"""
    Função len() vem do inglês lenght de comprimento
    informa justamente o tamanho total
    Exemplo:
    nome = "Atila Felipe Onaya"
    len(nome)
"""
print("Função len()")
nome = "Atila Felipe Onaya"
print(len(nome))

print("\n")

"""
    Função lower() retorna a string com caracteres minúsculos
    Exemplo:
    nome = "Natalia Yure Onaya"
    nome.lower()
"""
print("Função lower()")
nome = "Natalia Yure Onaya"
print(nome.lower())

print("\n")

"""
    Função upper() retorna a string com caracteres maiúsculos
    Exemplo:
    nome = "Leila Augusta de Oliveira Onaya"
    nome.upper()
"""
print("Função upper()")
nome = "Natalia Yure Onaya"
print(nome.upper())

print("\n")

"""
    Função split() retorna a string separadamente
    Exemplo:
    nome = "Daniel de Sousa Onaya"
    nome.split()

    Atenção a função split() só separa as palavras se a string já vinher com espaço!
"""
print("Função split()")
nome = "Daniel de Sousa Onaya"
print(nome.split())
nome = "KazuShikoOnaya"
print(nome.split())
