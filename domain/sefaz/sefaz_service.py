from domain.consultar_tributo.tributo_service import TributoCacheService


class SefazService:
    def __init__(self):
        self.tributo_cache_service = TributoCacheService()

    def gerar_produtos(self, venda_request):
        produtos = []
        for item in venda_request['itens']:
            produto = self.gerar_produto(item)
            produtos.append(produto)
        return produtos

    def gerar_produto(self, item):
        sku = item['sku']
        tributo_response = self.tributo_cache_service.consultar_com_cache(sku)
        return tributo_response
