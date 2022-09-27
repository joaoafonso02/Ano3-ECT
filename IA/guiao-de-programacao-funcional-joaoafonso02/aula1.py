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
	if lista == []:
		return True
	if lista[0] != lista[-1]: return False
	return capicua(lista[1:-1])

#Exercicio 1.7
def explode(lista):
	if not lista: 
		return lista
	return lista[:1][0] + explode(lista[1:])

#Exercicio 1.8
def substitui(lista, original, novo):
	if not lista: 
		return lista
	if lista[0] == original:
		return [novo] + substitui(lista[1:], original, novo)
	else:
		return lista[:1] + substitui(lista[1:], original, novo)

#Exercicio 1.9
def junta_ordenado(lista1, lista2):
	if not lista1:
		return lista2
	if not lista2:
		return lista1
	if lista1[0] < lista2[0]:
		return lista1[:1] + junta_ordenado(lista1[1:], lista2)
	else:
		return lista2[:1] + junta_ordenado(lista1, lista2[1:])


#Exercicio 2.1
def separar(lista):
	if not lista:
		return [], []
	a, b = lista[0]
	c, d = separar(lista[1:])
	return [a] + c, [b] + d

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if lista == []:
		return [], 0
	a, b = remove_e_conta(lista[1:], elem)

	if lista[0] == elem:
		return a, b+1
	else:
		return  [lista[0]]+a, b


#Exercicio 3.1
def cabeca(lista):
	if lista == []:
		return []
	return lista[0]

#Exercicio 3.2
def cauda(lista):
	if lista == []:
		return [] 
	return lista[1:]

#Exercicio 3.3
def juntar(l1, l2):
	if len(l1)!=len(l2) :
		return None

	if l1==[]:
		return l1
	
	a,b = l1[0],l2[0]

	return [(a,b)]+juntar(l1[1:],l2[1:])

#Exercicio 3.4
def menor(lista):
	if lista == []:
		return None
	min = menor(lista[1:])

	if min == None or lista[0] < min:
		return lista[0]
	else:
		return min

#Exercicio 3.6
def max_min(lista):
	if lista == []:
		return None
	
	min, max = max_min(lista[1:])

	if (min, max)  == (None, None):
		return lista[0], lista[0]
	if lista[0] < min:
		return lista[0], min
	if lista[0] > max:
		return lista[0], max
	return max, min
