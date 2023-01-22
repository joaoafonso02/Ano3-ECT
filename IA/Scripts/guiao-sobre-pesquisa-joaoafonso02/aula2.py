#Exercicio 4.1
impar = lambda x: x % 2 != 0 

#Exercicio 4.2
positivo = lambda x: x > 0 and x != 0 

#Exercicio 4.3
comparar_modulo = lambda a, b: abs(a) < abs(b) 

#Exercicio 4.4
cart2pol = None

#Exercicio 4.5
ex5 = None

#Exercicio 4.6
def quantificador_universal(lista, f):
    if lista == []:
        return True

    return f(lista[0]) and quantificador_universal(lista[1:], f)

def subconjunto(lista1, lista2):
    if lista1 == []:
        return True

    return lista1[0] in lista2 and subconjunto(lista1[1:], lista2)

#Exercicio 4.9
def ordem(lista, f):
    pass

#Exercicio 4.10
def filtrar_ordem(lista, f):
    pass

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
