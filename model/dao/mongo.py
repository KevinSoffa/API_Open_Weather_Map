from pymongo import MongoClient
from decouple import config # Variaveis no arquivo .env

# Conexão com o Banco de Dados Mongo
client = MongoClient(
    config('MONGO_URL')
)

db = client[f'{config("MONGO_DB")}']
