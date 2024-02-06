# Open Weather Map - Kevin Soffa

Este projeto consiste na criação de uma API REST em Python/FastAPI que fornece dados da previsão do tempo para os próximos cinco dias. Após consumir a API da Open Weather Map, o histórico das consultas é armazenado em um banco de dados MongoDB para consultas futuras.

## Instalação
### Requisitos
- Python 3.11 ou superior

### Comando para instalar Bibliotecas
Execute o seguinte comando no terminal com o ambiente virtual ativado:
```
pip install -r requirements.txt
```


#### Arquivo .env
Há um arquivo .env com as variavéis de ambiente, como; conexão com banco de dados Mongo DB, parametros de end pont, e configurações do FastApi. Ex:

CORS_ALLOWED=*

PREFIXO=/kevin

MONGO_URL=mongodb://localhost:27017/

MONGO_DB=raizen_tech

## Rotas
### Consulta API da Open Weather Map para trazer dados dos últimos 5 dias
**GET** ```/kevin?lat={lat}&lon={lon}&api_key={api_key}```

QueryParams
- lat: Latitude a ser pesquisada
- lon: Longitude a ser pesquisada
- api_key: Token para validação e consumo da API (https://home.openweathermap.org/api_keys)

exemplo de resposta HTTP 200OK:
```
{
    "cod": "200",
    "message": 0,
    "cnt": 40,
    "list": [
        {
            "dt": 1702317600,
            "main": {
                "temp": 297.23,
                "feels_like": 297.73,
                "temp_min": 296.04,
                "temp_max": 297.23,
                "pressure": 1014,
                "sea_level": 1014,
                "grnd_level": 926,
                "humidity": 78,
                "temp_kf": 1.19
            },
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": {
                "all": 76
            },
            "wind": {
                "speed": 3.88,
                "deg": 176,
                "gust": 4.66
            },
            "visibility": 10000,
            "pop": 0.99,
            "rain": {
                "3h": 2.58
            },
            "sys": {
                "pod": "d"
            },
            "dt_txt": "2023-12-11 18:00:00"
        }   
    ],
    "city": {
        "id": 3448439,
        "name": "São Paulo",
        "coord": {
            "lat": -23.5489,
            "lon": -46.6388
        },
        "country": "BR",
        "population": 10021295,
        "timezone": -10800,
        "sunrise": 1702282391,
        "sunset": 1702331185
    }
}
```

### Consulta Histórico no Banco de dados (todos os dados)
**GET ALL** ```/kevin/historico```

exemplo de resposta HTTP 200OK:
```
{
    "historico": [
        {
            "city": "Guarulhos",
            "lat": -23.413,
            "lon": -46.4445,
            "temp": 22.16,
            "date": "2023-12-11T14:00:59.284000",
            "id": "6577404bb0cea08c0daed9f9"
        },
        {
            "city": "São Paulo",
            "lat": -23.5489,
            "lon": -46.6388,
            "temp": 22.08,
            "date": "2023-12-11T15:24:47.800000",
            "id": "657753ef8cb62ae339b32819"
        }
    ]
}
```

### Consulta Histórico por ID:
**GET ID** ```/kevin/historico/{id}```

exemplo de resposta HTTP 200OK  
```
{
    "city": "Guarulhos",
    "lat": -23.413,
    "lon": -46.4445,
    "date": "2023-12-11T14:00:59.284000",
    "id": "6577404bb0cea08c0daed9f9"
}
```

### Consulta Histórico por City(cidade):
**GET CITY** ```/kevin/historico/city/{city}```

exemplo de resposta HTTP 200OK:
```
{
    "city": "São Paulo",
    "lat": -23.5489,
    "lon": -46.6388,
    "temp": 22.08,
    "date": "2023-12-11T15:24:47.800000",
    "id": "657753ef8cb62ae339b32819"
}
```

### Consulta Histórico Lat e Lon (latitude e longitude):
**GET LAT e LON** ```/kevin/historico/lat/{lat}/lot/{lot}```

exemplo de resposta HTTP 200OK:
```
{
    "city": "São Paulo",
    "lat": -23.5489,
    "lon": -46.6388,
    "date": "2023-12-11T15:24:47.800000",
    "id": "657753ef8cb62ae339b32819"
}
```
