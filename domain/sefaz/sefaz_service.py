import logging
from dataclasses import asdict

from domain.sefaz.authorize_request import AuthorizeRequest
from domain.sefaz.customer import Customer
from domain.sefaz.product import Product
from infrastructure.provider.sefaz_client import SefazClient
from infrastructure.provider.tributo_client import TributoClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SefazService:
    def __init__(self):
        self.tributo_client = TributoClient()
        self.sefaz_client = SefazClient()

    def authorize_sale(self, venda_request):
        authorize_request = self._generate_sales_request(venda_request)
        authorize_request_dict = asdict(authorize_request)

        return self.sefaz_client.authorize(authorize_request_dict)

    def _generate_sales_request(self, venda_request):
        customer = self._gerar_customer(venda_request['cliente'])
        products = self._gerar_produtos(venda_request)
        return AuthorizeRequest(
            orderNumber=venda_request['ordemPedido']['numeroPedido'],
            externalOrderNumber=venda_request['ordemPedido']['numeroOrdemExterno'],
            customer=customer,
            products=products
        )

    @staticmethod
    def _gerar_customer(cliente):
        return Customer(
            id=cliente['id'],
            name=cliente['nome'],
            document=cliente['documento'],
            documentType=cliente['tipoDocumento'],
            personType=cliente['tipoPessoa'],
            address=cliente['endereco'],
            addressNumber=cliente['numeroEndereco'],
            addressComplement=cliente['complementoEndereco'],
            district=cliente['bairro'],
            city=cliente['cidade'],
            state=cliente['estado'],
            country=cliente['pais'],
            zipCode=cliente['cep'],
            ibgeCode=cliente['codigoIbge'],
            phoneNumber=cliente['telefone'],
            email=cliente['email'],
        )

    def _gerar_produtos(self, venda_request):
        produtos = []
        for item in venda_request['itens']:
            produto = self._gerar_produto(item)
            produtos.append(produto)
        return produtos

    def _gerar_produto(self, item):
        tributo_response = self.tributo_client.consultar_tributo(item['sku'])
        return Product(
            sku=item['sku'],
            amount=item['quantidade'],
            value=self._multiply_by_hundred(value=item['valor']),
            icmsValue=tributo_response['valorIcms'],
            pisValue=tributo_response['valorPis'],
            difaulValue=tributo_response['valorDifaul'],
            fcpIcmsValue=tributo_response['valorFcpIcms'],
        )

    @staticmethod
    def _multiply_by_hundred(value):
        return value * 100
