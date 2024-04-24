from flask_restx import fields

from domain.authorize_sale.model.client_model import ClientModel
from domain.authorize_sale.model.item_model import ItemModel
from domain.authorize_sale.model.order_model import OrderModel


class AuthorizeSaleModel:
    @staticmethod
    def get_model(api):
        return api.model('AutorizarVenda', {
            'canal': fields.String(required=True, description='Canal de venda', example='APP'),
            'empresa': fields.String(required=True, min_length=5, max_length=5, description='Código da empresa',
                                     example='00001'),
            'loja': fields.String(required=True, min_length=4, max_length=4, description='Código da loja',
                                  example='0001'),
            'pdv': fields.Integer(required=True, min_value=1, description='Número do ponto de venda', example=501),
            'ordemPedido': fields.Nested(ClientModel.get_model(api), required=True,
                                         description='Detalhes da ordem de pedido'),
            'cliente': fields.Nested(ItemModel.get_model(api), required=True, description='Detalhes do cliente'),
            'totalItens': fields.Integer(required=True, min_value=1, description='Total de itens na venda',
                                         example=38744),
            'quantidadeItens': fields.Integer(required=True, min_value=1, description='Quantidade de itens distintos',
                                              example=6),
            'itens': fields.List(fields.Nested(OrderModel.get_model(api)), description='Lista de itens da venda')
        })
