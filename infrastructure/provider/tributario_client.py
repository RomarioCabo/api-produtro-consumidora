from dataclasses import dataclass
from decimal import Decimal

# import requests


@dataclass
class TributoResponse:
    sku: int
    valor_icms: Decimal
    valor_pis: Decimal
    valor_difaul: Decimal
    valor_fcp_icms: Decimal


class ConsultadorTributoService:
    def consultar(self, sku):
        return TributoResponse(sku=sku, valor_icms=Decimal('100.00'), valor_pis=Decimal('50.00'),
                               valor_difaul=Decimal('20.00'), valor_fcp_icms=Decimal('30.00'))


class TributarioClient:
    def __init__(self, base_url='http://localhost:9585/template/'):
        self.base_url = base_url
        self.consultador_tributo_service = ConsultadorTributoService()

    def consultar_tributo(self, sku):
        return self.consultador_tributo_service.consultar(sku)
        # url = f"{self.base_url}tributo"
        # headers = {'Content-Type': 'application/json'}
        # response = requests.get(url, headers=headers, params={'sku': sku})
        #
        # if response.status_code == 200:
        #     return response.json()
        # else:
        #     response.raise_for_status()
