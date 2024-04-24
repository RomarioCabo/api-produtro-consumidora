from flask_restx import fields


class ItemModel:
    @staticmethod
    def get_model(api):
        return api.model('Item', {
            'sku': fields.Integer(
                required=True,
                description='SKU (Stock Keeping Unit) do item, identificador único do produto no estoque.',
                example=3355991002319,
                min=1  # Garante que o valor seja pelo menos 1
            ),
            'quantidade': fields.Integer(
                required=True,
                description='Quantidade do item na ordem.',
                example=1,
                min=1  # Garante que a quantidade seja pelo menos 1
            ),
            'valor': fields.Integer(
                required=True,
                description='Valor do item em centavos.',
                example=5000,
                min=1  # Garante que o valor seja pelo menos 1
            )
        })
