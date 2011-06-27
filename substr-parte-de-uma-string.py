string = "Meu teste com string"

#resgatar os caracteres que ficam entre o primeiro e o ultimo
print string[1:-1]

#resgatar todos caracteres, menos os 5 ultimos caracteres
print string[0:-5]

#resgatar todos caracteres, menos os 5 primeiros
print string[5:]

#resgatar todos caracteres, menos os 5 ultimos caracteres 
#[Outra forma de escrever]
print string[:-5]

#se os dois indices passados forem iguais o resultado e vazio
print string[5:5]

#ao utilizar o segundo parametro com um indice maior que zero
#ele serivira como limite, ouseja, neste caso sera impresso do
#caracter 1 ate o quinto caracter da string, que eh o limite
print string[1:5]

#se os dois parametros forem vazios eh retornada a string inteira
print string[:]

#e ao contrario acontece se passarmos os dois parametros com indices
#que nao existem, numeros maiores que os indices existentes no vetor
print string[52:38]
