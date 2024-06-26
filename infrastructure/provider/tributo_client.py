import requests


class TributoClient:
    def __init__(self, base_url='http://localhost:8081/api/v1/'):
        self.base_url = base_url

    def consultar_tributo(self, sku):
        url = f"{self.base_url}tributo"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers, params={'sku': sku})

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
