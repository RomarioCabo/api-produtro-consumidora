from infrastructure.provider.tributo_client import TributoClient


class SefazService:
    def __init__(self):
        self.tributo_client = TributoClient()

    def gerar_produtos(self, venda_request):
        produtos = []
        for item in venda_request['itens']:
            produto = self._gerar_produto(item)
            produtos.append(produto)
        return produtos

    def _gerar_produto(self, item):
        sku = item['sku']
        tributo_response = self.tributo_client.consultar_tributo(sku)
        return tributo_response
