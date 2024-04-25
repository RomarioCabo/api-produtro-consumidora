import requests


class SefazClient:
    def __init__(self, base_url='http://localhost:8081/api/v1/'):
        self.base_url = base_url

    def authorize(self, authorize_request):
        url = f"{self.base_url}authorize"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, json=authorize_request)

        if response.status_code == 200 or response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
