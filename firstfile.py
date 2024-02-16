import json
import requests

url_btc = "https://api.polygon.io/v1/open-close/crypto/BTC/USD/2023-01-09?adjusted=true&apiKey=pt42fCZ3HUMSpYOy1PE_EPB1CAxpzms9"


res_btc = requests.get(url_btc)
data_btc = res_btc.json()
print(json.dumps(data_btc,indent=4))

url_eth = "https://api.polygon.io/v1/open-close/crypto/ETH/USD/2023-01-09?adjusted=true&apiKey=pt42fCZ3HUMSpYOy1PE_EPB1CAxpzms9"

res_eth = requests.get(url_eth)
data_eth = res_eth.json()
print(json.dumps(data_eth,indent=4))