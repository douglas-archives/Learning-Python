# Para estudo de mais dicas basta ir direto a fonte que foram retirados os exemplos:
#  http://www.siafoo.net/article/52

# Voce pode incorporar certas estruturas de codigo em lugares bem diferentes em Python
# Por exemplo um for dentro de um if
numbers = [1,10,100,1000,10000]
if [number for number in numbers if number < 10]:
    print 'O elemento menor que 10 foi encontrado!'
# No exemplo acima, assim que a condicao for veradeira o laco eh interrompido e 
# o codigo que estiver dentro do condicional if sera executado, neste caso o print


# Mas podemos fazer melhor ainda, se quisermos executar algo 
# se alguma condicao do laco for verdadeira, basta usar o 'any'
numbers = [1,10,100,1000,10000]
if any(number < 10 for number in numbers):
	print 'Success'


# E para executar algo se todas as condicoes forem verdadeiras podemos
# utilizar a funcao 'all'
numbers = [1,2,3,4,5,6,7,8,9]
if all(number < 10 for number in numbers):
    print 'Success!'

# ------------------------------------------------------------------------

# Podemos utilizar o laco for dentro de um print
print [(x, y, x * y) for x in (0,1,2,3) for y in (0,1,2,3) if x < y]
# Nesse exemplo acima, ele executara a conta (x, y, x * y) 
# toda vez que no segundo 'for' o X for menor que o Y

# ------------------------------------------------------------------------

# Combinar listas com zip
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
squares = [1, 4, 9]

zipped_list = zip(letters, numbers, squares)
print zipped_list


# Vamos utilizar as listas acima para mostrar outras funcoes disponiveis
# para trabalhar com listas

# Retorna o maior elemento da lista, seja string ou numeros
print max(squares)

# Retorna o menor elemento da lista, seja string ou numeros
print min(letters)

# Retorna a soma dos elementos da lista, neste strings nao sao suportadas
# se quiser unir as strings use o join, por exemplo: print "".join(letters)
print sum(squares)

# ------------------------------------------------------------------------

# Strings
# trabalhando com strings em relacao ao estado booleano delas

my_object = 'Test' # Verdadeiro quando NAO for vazio
#  my_object = '' # ... e falso quando for fazio

if len(my_object) > 0:
	print 'my_object nao esta vazio 1'

if len(my_object):  # 0 sera encarado como False
	print 'my_object nao esta vazio 2'

if my_object != '':
	print 'my_object nao esta vazio 3'

if my_object: # uma string vazia sera encarada como falsa (False)
	print 'my_object nao esta vazio 4'

# ------------------------------------------------------------------------

# Um exemplo de como Python eh flexivel para resolver problemas de diferentes
# formas, porem para maior legibilidade e elegancia de codigo encontramos 
# sempre uma forma melhor de resolver determinado problema

# Neste exemplo queremos saber o quadrado de cada numero da lista (numbers) e
# armazenar os valores em outra lista
 
numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    squares.append(number*number)
print squares
# voce tera [1,4,9,16,25]
# voce de fato consegui chegar ao objetivo, com bastantes linhas mas o fez

# podemos dimimuir esse codigo e usufruir da funcao map mapear esta lista
numbers = [1,2,3,4,5]
squares = map(lambda x: x*x, numbers)
print squares
# voce tera  [1,4,9,16,25]
# O codigo chega ao objetivo, eh mais curto, porem um pouco mais complexo e 'feio'
# a utilizacao de map e lambda, neste caso, acabam complicando o simples problema

# vamos usufruir list comprehension que o Python oferece
numbers = [1,2,3,4,5]
squares = [number*number for number in numbers]
# entenda o que se passa dentro dos colchetes: 
# o calculo (number*number) sera executado cada ocorrencia do loop for number in numbers
# assim o resultado deste calculo sera armazenado em cada tupla da nova lista squares

print squares
# voce tera  [1,4,9,16,25]