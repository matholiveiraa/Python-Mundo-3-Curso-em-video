import urllib
import urllib.request
import requests

site = 'https://www.pudim.com.br/'


try:
    resposta = requests.get(site)
    if resposta.status_code == 200:
        print("Acessivel")
except:
        print(f"Erro ao acessar o site")
