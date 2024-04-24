from flask_restx import fields


class OrderModel:
    @staticmethod
    def get_model(api):
        return api.model('OrdemPedido', {
            'numeroPedido': fields.String(
                required=True,
                description='Número do pedido. Deve ser um número positivo.',
                example="82110612413",
                min_length=1,  # Garante que o campo não esteja em branco
                pattern=r'^\d+$'  # Garante que o campo seja numérico e positivo
            ),
            'numeroOrdemExterno': fields.String(
                required=True,
                description='Código externo da ordem. Deve seguir o padrão numérico positivo com dígito separador.',
                example="123456789101-1",
                pattern=r'^[0-9]+(-[0-9]+)?$'  # Padrão para números com possíveis dígitos separadores
            ),
            'dataAutorizacao': fields.DateTime(
                required=True,
                description='Data e hora da autorização da ordem.',
                example="2022-11-11T15:37:56.194",
                dt_format='iso8601'  # Formato ISO 8601 para data e hora
            )
        })
