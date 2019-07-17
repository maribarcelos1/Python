import requests

palavra = str(input("Digite uma palavra.: "))
parameter = {"rel_rhy":str(palavra)} # passando o parametro , rel_rhy é uma palavra chave da api para buscar as palavras mais semelhantes

#chama o site passando os parametros como filtro
requests = requests.get('https://api.datamuse.com/words',parameter)

json = requests.json()
if len(json) < 1:
    print('\nErro.: palavra buscada não encontrada')
else:
    for i in json[0:3]:
        print(i['word'])

#fazer uma excessao de resposta