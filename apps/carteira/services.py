import requests

def obter_taxa_cambio(moeda_origem, moeda_destino):
    api_key = 'SUA_CHAVE_FIXER_API'
    url = f'http://data.fixer.io/api/latest?access_key={api_key}&base={moeda_origem}&symbols={moeda_destino}'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados['rates'][moeda_destino]