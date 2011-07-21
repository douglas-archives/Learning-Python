"""
Numeros decimais para Romanos
Fazendo de uma forma otimizada sem digitar muito codigo podemos fazer da seguinte forma:

Observe que na tabela abaixo ha apenas ate 3 milhoes, em numerais romanos e complicado
trabalhar com grandes numeros, pois para representar os mesmos pode-se fazer
representacoes inviaveism, exemplo vamos mapear a tabela de simbolos ate o limite
estabelecido nela, de qualquer modo com o tempo, talvez otimize para ficar mais claro.
"""

symbols = {
			1:['',  'I',   'II',   'III',   'IV',   'V',   'VI',   'VII',   'VIII',   'IX' ],  # unidades
			2:['',  'X',   'XX',   'XXX',   'XL',   'L',   'LX',   'LXX',   'LXXX',   'XC' ],  # dezenas
			3:['',  'C',   'CC',   'CCC',   'CD',   'D',   'DC',   'DCC',   'DCCC',   'CM' ],  # centenas
			4:['',  'M',   'MM',   'MMM',  '(IV)', '(V)', '(VI)', '(VII)', '(VIII)', '(IX)'],  # milhares
			5:['', '(X)', '(XX)', '(XXX)', '(XL)', '(L)', '(LX)', '(LXX)', '(LXXX)', '(XC)'],  # dezenas de milhares
			6:['', '(C)', '(CC)', '(CCC)', '(CD)', '(D)', '(DC)', '(DCC)', '(DCCC)', '(CM)'],  # centenas de milhares
			7:['', '(M)', '(MM)', '(MMM)',     '',    '',     '',      '',       '',     '']   # milhoes
		}
# o limite e 3999999
number = str(1251)
size = len(number)

print ''.join([symbols[size-x][int(number[x])] for x in xrange(0, size)])