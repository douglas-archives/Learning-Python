# Este eh o programa que testa se uma palavra e palindrome
# Da forma como segue abaixo e facil para entendermos o uso de funcoes,
# um pouco de trabalho com strings e seguir passo a passo para
# melhor entendimento

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if first(word) == last(word):
		if len(word) == 1:
			return True
		else:
			return is_palindrome(middle(word))
	else:
		return False

# Tests
print is_palindrome('ana')
print is_palindrome('maria')
print is_palindrome('jose')
print is_palindrome('banana')
print is_palindrome('aba')
print is_palindrome('cururuc')

# A versao abaixo, que esta comentada, e outra forma de se fazer a mesma 
# funcao, com o mesmo resultado, porem de uma forma mais curta e direta
# sem a divisao dos trabalhos, mas para iniciantes talvez possa ser dificil

# def is_palindrome(word):
# 	if len(word) == 0:
# 		return True
# 	return is_palindrome(word[1:-1]) if word[0] == word[-1] else False