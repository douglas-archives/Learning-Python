#Isto e um comentario!
#A documentacao esta sem acento para nao ocasionar erros
#Imprime a string passada entre quotes em tela
print 'Hello World!'

#Se voce tem duvidas de qual e o tipo de variavel que voces esta tragalhando
#Utilize o type(var) para descobrir
print type('Hello World!')
print type(7)

#Se voce precisar escrever um 'inteiro longo' ele nao deve ser escrito como no
#exemplo abaixo, pois sera interpretado diferente.
print 1,000,000
#ou seja, nao sera um erro de sintaxe, porem nao funcionara da forma como voce
#espera

#As variaveis sao bem simples

message = 'And now for something completely different'
print message
n = 17
print n
pi = 3.1415926535897931
print pi


#Os nomes de variaveis devem comecar com letra e terminar com letra, podendo haver
#numeros no meio do nome, bem como letras maiusculas e underline (_)
#Deve se estar atento as keywords
#Os tres exemplos abaixo sao ilegais
#comecando com um numero
#76trombones = 'big parade'
#caracter ilegal
#more@ = 1000000
#palavra reservada, ou seja, uma keyword do python 'class'
#class = 'Advanced Theoretical Zymurgy'

#basicamente as keywords do python sao:
'''
and
as
assert
break
class
continue
def
del
elif
else
except
exec
finally
for
from
global
if
import
in
is
lambda
not
or
pass
print
raise
return
try
while
with
yield
'''

#Tecnicamente a impressao abaixo deveria ser: 02132, porem e: 1114
print 02132
#comencando com um 0 o interpretador entende, como no php, que o valor e binario
#para testes tente imprimeir os numeros: 01, 010, 0100 e 01000

#Operadores, eles sao, basicamente, simples
print 5+2
print 5-2
print 5*2
print 5/2
#Exponeciacao, em algumas linguagens utiliza-se o circunflexo, 
#mas em python usa-se **
print 5**2

#Simples mas em caso de resultados float, no python 2.* ainda ha o problema
#com divisao de 2 inteiros e um resultado float, por exemplo:
print 59/60
#deveria retornar 0.98333, porem retornara 0
#para resolver isto, por enquanto, podemos usar o .0 ou o float(int)
print 59.0/60
print float(59)/60

#erro de divisao por zero
# print 5/0

#Nao importa se as strings guardarem numeros o operador + somente vai fazer o
#trabalho de concatenacao e nao de soma
first = '1'
second = '2'
print first + second

#...se utilizarmos o * ele executara a funcao de multiplicar, porem multiplicara 
#a quantidade de strings, ou seja, o output do exemplo abaixo sera:
#oh yeah! oh yeah! oh yeah!  
print 'oh yeah! '*3

#olhe este print que simula o printf() do C, ou sprintf()  do PHP
#a proposito note que o \ serve para quebrar a linha neste caso que estamos
#em meio a uma expressao
print "Meu nome eh %s, e eu tenho %d anos e %f de altura. " % \
	  ("Douglas", 21, 1.68)