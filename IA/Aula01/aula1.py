#Exercicio 1.1
def comprimento(lista):
	if lista == []:
		return 0
	return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if lista == []:
		return 0
	return lista[0] + soma(lista[1:])

#Exercicio 1.3
def existe(lista, elem):
	if lista == []:
		return False
	return lista[0] == elem or existe(lista[1:], elem)

#Exercicio 1.4
def concat(l1, l2):
	if l1==[] and l2==[]:
		return l1

	if l2==[]:
		return l1

	l1.append(l2[0])
	return concat(l1,l2[1:])

#Exercicio 1.5
def inverte(lista):
	if lista == []:
		return []
	return [lista[-1]] + inverte(lista[:-1]) # whats the diff having braces or not?

#Exercicio 1.6
def capicua(lista):
	if lista == [] or len(lista) == 1:
		return True
	return lista[0] == lista[-1] and capicua(lista[1:-1])

#Exercicio 1.7
def explode(lista):
	pass

#Exercicio 1.8
def substitui(lista, original, novo):
	pass

#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	pass

#Exercicio 2.1
def separar(lista):
	pass

#Exercicio 2.2
def remove_e_conta(lista, elem):
	pass

#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
    pass

#Exercicio 3.4
def menor(lista):
	pass

#Exercicio 3.6
def max_min(lista):
	pass
