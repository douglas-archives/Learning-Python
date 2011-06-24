#quando passo strings o metodo sort() ordena por ordem alfabetica
lista_string = ['bbb', 'yyy', 'mmm', 'aaa', 'www', 'ddd']
lista_string.sort()
print lista_string

#ao passar numeros a lista sera ordenada do menor para o maior
lista_numeros = [521, 123, 52, 5, 546546536]
lista_numeros.sort()
print lista_numeros

lista_numeros = [521, 123, 52, 5, 546546536]
lista_numeros.sort()
print lista_numeros

#Caso eu queira listar de acordo com o tamanho da string...
lista = ['aaaa', 'z', 'bbbbbbbbbb', 'nnn']
def porTamanho(item):
    return len(item)

print sorted(lista, key=porTamanho)

#se eu quiser embaralhar a lista acima...
import random
random.shuffle(lista)
print lista