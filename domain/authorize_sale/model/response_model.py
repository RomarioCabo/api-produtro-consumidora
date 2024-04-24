from flask_restx import fields


class ResponseModel:
    @staticmethod
    def get_model(api):
        return api.model('AuthorizeSaleResponse', {
            'status': fields.String(required=True, description='Status da venda', example='EM_PROCESSAMENTO'),
            'timestamp': fields.DateTime(dt_format='iso8601', required=True,
                                         description='Hora do processamento', example='2022-11-11T15:37:56.194')
        })
