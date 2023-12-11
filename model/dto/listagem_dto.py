from dataclasses import dataclass
from fastapi import Query


@dataclass
class ListagemDTO:
    # Queryparams que são passados para a requisição da API
    lat: float = Query(...)
    lon: float = Query(...)
    api_key: str = Query(...)
