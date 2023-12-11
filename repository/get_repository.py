from requests import request


# Faz a requisição GET na API Open Wather Map
def get_repository(dto: dict):

    listagem = request(
        'GET',
        url = 'http://api.openweathermap.org/data/2.5/forecast?units=metric&lat=%s&lon=%s&appid=%s' % (dto['lat'], dto['lon'], dto['api_key']),
        headers={
            'Content-Type':'application/json'
        }

    )

    resposta = listagem.json()

    #retorna reposta da API
    return resposta
