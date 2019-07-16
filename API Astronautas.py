import requests

#chama o site
request = requests.get('http://api.open-notify.org')
#print(request.text)

#se o site estiver rodando é 200
#print(request.status_code)


#se o site estiver fora 404
request2 = requests.get('http://api.open-notify.org/fake-endpoint')
#print(request2.status_code)


#chama api de localização
iss_position = requests.get('http://api.open-notify.org/iss-now.json')

#melhorando API
iss_position_json = iss_position.json()

#print('Local atualizado em Latitude e Longitude é: ', iss_position['iss_position'])

#traz as pessoas que estao no espaço esse momento
people = requests.get('http://api.open-notify.org/astros.json')
#print(people.text)

#modo mais facil de utilizar os dados de " para '
people_json = people.json()
#print(people_json)

#printar as numero de pessoas no espaço
print("Número de pessoas no espaço AGORA:",people_json['number'])

#printar os nomes das pessoas no espaço
for p in people_json['people']:
    print('Nome:',p['name'])


