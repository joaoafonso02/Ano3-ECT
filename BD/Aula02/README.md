## Aula P02

# P1G7 - Membros
[João Afonso Ferreira](https://github.com/joaoafonso02), 103037  
[Eduardo Fernandes](https://github.com/EduardoFernandesUA), 102648  

## Exercício 2.1

# a)
| Entidades  	| Atributos                                                  	|
|------------	|------------------------------------------------------------	|
|   Produto  	|             Código<br>Preço<br>Nome<br>Taxa IVA            	|
|   Empresa  	|                         Nome<br>NIF                        	|
| Encomenda  	| Número <br>Data                                            	|
| Fornecedor 	| NIF <br>Nome <br>Endereço <br>Fax <br>Pagamento <br>Código 	|

# b)
|        Relação        	| Grau 	| Cardinalidade 	| Obrigatoriedade de Participação 	|
|:---------------------:	|:----:	|:-------------:	|:-------------------------------:	|
|   Empresa --> Produto   	|   2  	|      1:N      	|             Produto             	|
|  Produto --> Encomenda  	|   2  	|      M:N      	|            Encomenda            	|
| Encomenda --> Forncedor 	|   2  	|      N:1      	|            Encomenda            	|