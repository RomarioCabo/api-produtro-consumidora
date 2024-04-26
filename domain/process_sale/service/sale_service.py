import json
import logging
from datetime import datetime

from infrastructure.persistence.sale.sale_entity import SaleEntity
from infrastructure.persistence.sale.sale_repository import SaleRepository

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SaleService:
    def __init__(self):
        self.sale_repository = SaleRepository()

    def save(self, venda_request, authorize_response):
        new_sale = SaleEntity(
            canal=venda_request['canal'],
            codigo_empresa=venda_request['empresa'],
            codigo_loja=venda_request['loja'],
            numero_pdv=venda_request['pdv'],
            numero_pedido=venda_request['ordemPedido']['numeroPedido'],
            numero_ordem_externo=venda_request['ordemPedido']['numeroOrdemExterno'],
            valor_total=self._multiply_by_hundred(value=venda_request['totalItens']),
            quantidade_itens=venda_request['quantidadeItens'],
            venda_request=self._dict_to_json_string(data=venda_request),
            data_atualizacao=datetime.now(),
            data_requisicao=venda_request['ordemPedido']['dataAutorizacao'],
            chave_nfe=authorize_response['nfeKey'],
            numero_nota=authorize_response['invoiceNumber'],
            data_emissao=authorize_response['issuanceDate'],
            pdf=authorize_response['invoice'],
            situacao='Processado',
            motivo='',
        )
        self.sale_repository.save(new_sale)

    @staticmethod
    def _multiply_by_hundred(value):
        return value * 100

    @staticmethod
    def _dict_to_json_string(data):
        return json.dumps(data)
