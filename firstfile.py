import json
import requests

url = "https://api.polygon.io/v1/open-close/crypto/BTC/USD/2023-01-09?adjusted=true&apiKey=pt42fCZ3HUMSpYOy1PE_EPB1CAxpzms9"


res = requests.get(url)
data = res.json()
print(json.dumps(data,indent=4))

