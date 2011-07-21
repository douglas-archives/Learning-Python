#!/usr/bin/env python
# O laco for. O i que recebe o valor inteiro, incrementado a cada repeticao do laco
# note que para imprimir o i juntamente com outro texto, ou seja, concatenar
# uma string com um inteiro e necessario realizar a conversao do inteiro para string
# neste caso o laco ira de 1 ate 3
for i in range(1,4):
	print 'Hello! ' + str(i)

# Temos a alteranativa xrange, faz a mesma coisa mas possui efeitos de desempenho
# diferentes.
for i in xrange(1,4):
	print 'Hello! ' + str(i)

# EXPLICACAO: range(1,4), por exemplo, cria uma lista de 1 ate 3, desta forma>>
# [1, 2, 3], assim se houver 1.000.000.000 de posicoes essa funcao criara, e armazenara
# em memoria uma lista com um milhao de posicoes.
# Ja o xrange(1,4), se voce mandar imprimir vera que ele eh um objeto xrange e nao uma lista
# e o que ele faz de diferente eh criar os itens sob-demanda, ou seja, ele cria item por item
# baseado nos parametros recebidos, assim ele ocupa somente 'um espaco de memoria' por vez


# Utilizando uma string. Note que ha uma virgula apos a impressao da variavel
# isto faz com que a saida no terminal ocorra inline, ou seja, nao havera
# quebra de linha
for letra in 'Douglas Miranda':
    print letra,

print '\n'

#quando for usar o for, por exemplo, baseado em um tamanho de string
#voce poderia fazer da forma abaixo:
strings = ['a', 'b', 'c', 'd', 'e']
for index in xrange(len(strings)):
    print index,

print '\n'

#Porem para este caso o Python tem o enumerate() que melhora este algoritmo acima
for index, string in enumerate(strings):
	print index, ' => ', string

print '\n'

a = 0
while a < 3:
	a+=1
	print 'test'

# utilizando o laco for dentro do retorno de uma funcao
# desta forma consigo resumir bem oque teria de fazer do modo convencional
def return_values():
	return [value for value in ['a','b','c']]

print return_values()

# nesta forma de loop eu consigo extrair esses valores
# que, neste caso, cada elemento da lista eh uma tupla 
# que contem pares de elementos armazenados
for x, y in [('a','b'), ('c', 'd'), ('e', 'f')]:
	print x, y