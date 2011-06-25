#if, else, elif
x = 5; y = 3

#Observe que o delimitador de bloco eh a identacao
if x < y:
	print 'x e menor que y'
elif x > y: # observe que o que geralmente chamanos de 'else if', em python e 'elif'
	print 'x e maior que y'
else:
	if x == 5:
		print 'x eh igual a 5, entao y tbm e igual a 5'
	else:
		print 'x e y sao iguais'


# outro exemplo utilizando if, agora utilizando o a keyword 'and'
# observe que executo operacoes e comparo o resultado dentro do condicional
if x == 5 and x * y == 15:
	print 'x = 5 e (x * y) = 15'


if x == '5':
	print 'Yeah'
else:
	print '<int>x nao e igual a <string>5'	


# neste modelo estou utilizando o if dentro de uma funcao
# esta e uma funcao recursiva, neste caso utilizando a
# estrutura de controle 'if' para tomar a decisao
def countdown(n):
	if n <= 0:
		print 'Fim'
	else:
		print n
		countdown(n-1)

#chamada de funcao
countdown(3)
