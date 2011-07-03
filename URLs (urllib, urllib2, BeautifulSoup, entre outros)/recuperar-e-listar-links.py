"""
Exemplo extraido a partir do artigo de Herberth Amaral - @herberthamaral
http://herberthamaral.com/2010/02/criando-web-crawlers-em-python-parte-i/

Neste exemplo faremos o uso de urllib2 para requisitar a url
e resgatar o codigo-fonte completo do endereco requisitado.

Mais onformacoes sobre urllib2: 
http://www.voidspace.org.uk/python/articles/urllib2.shtml

E o modulo BeautifulSoup para manipulacao do codigo-fonte requisitado,
a fim de obter mais facilmente os objetos contidos no codigo.

BeautifulSoup, pode ser econtrado no endereco: 
http://pypi.python.org/pypi/BeautifulSoup/
"""
import urllib2
from BeautifulSoup import BeautifulSoup

# url a ser requisitada
url = "http://www.google.com"

# requisito a url
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# obtenho o conteudo requisitado
document = response.read()
#caso queira ver o retorno de response.read(), basta imprimir document
# print document

# normaliza o documento para que o mesmo seja acessivel via objetos
soup = BeautifulSoup(document) 

# agora que o retorno de minha requisicao ja esta em meu objeto soup
# posso usufruir das varias formas de tratamento do codigo de marcacao
# que a BeautifulSoup me oferece

# as nomenclaturas dos metodos sao explicitas, assim nao ha duvidas que
# na linha abaixo o metodo findAll retornara uma serie de links (<a>)
# encontrados no codigo-fonte que obtemos como resposta na requisicao
# feita pela urllib2
links = soup.findAll('a')  

# esta lista de links agora pode ser manipulada para apenas listarmos os links
# obtidos, ou podemos ate mesmo utilizar como chave o atributo que desejamos 
# obter dos links retornados, neste exemplo obtenho o valor do atributo href
# poderia tambem obter qualquer atributo de <a>, por exemplo, o class 
# link['class'] 
for link in links:
	print link['href']