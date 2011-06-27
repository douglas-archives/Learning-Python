#Voce pode incorporar certas estruturas de codigo em lugares bem diferentes em python
#Por exemplo um for dentro de um if
numbers = [1,10,100,1000,10000]
if [number for number in numbers if number < 10]:
    print 'O elemento menor que 10 foi encontrado!'
#No exemplo acima, assim que a condicao for veradeira o laco eh interrompido e 
#o codigo que estiver dentro do condicional if sera executado, neste caso o print

#Mas podemos fazer melhor ainda, se quisermos executar algo 
#se alguma condicao do laco for verdadeira, basta usar o 'any'
numbers = [1,10,100,1000,10000]
if any(number < 10 for number in numbers):
	print 'Success'

#E para executar algo se todas as condicoes forem verdadeiras podemos
#utilizar a funcao 'all'
numbers = [1,2,3,4,5,6,7,8,9]
if all(number < 10 for number in numbers):
    print 'Success!'

#Podemos utilizar o laco for dentro de um print
print [(x, y, x * y) for x in (0,1,2,3) for y in (0,1,2,3) if x < y]
#Nesse exemplo acima, ele executara a conta (x, y, x * y) 
#toda vez que no segundo 'for' o X for menor que o Y

#Combinar listas com zip
letters = ['a', 'b', 'c']
numbers = [1, 2, 3]
squares = [1, 4, 9]

zipped_list = zip(letters, numbers, squares)
print zipped_list

#vamos utilizar as listas acima para mostrar outras funcoes disponiveis
#para trabalhar com listas

#Retorna o maior elemento da lista, seja string ou numeros
print max(squares)

#Retorna o menor elemento da lista, seja string ou numeros
print min(letters)

#Retorna a soma dos elementos da lista, neste strings nao sao suportadas
#se quiser unir as strings use o join, por exemplo: print "".join(letters)
print sum(squares)
