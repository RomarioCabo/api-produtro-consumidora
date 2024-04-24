from flask_restx import Resource, Namespace
from domain.authorize_sale.model import authorize_sale_model, response_model
from domain.authorize_sale.service.authorize_sale_service import AuthorizeSaleService

api = Namespace('autorizar-venda', description='Autorização de vendas')


@api.route('/api/v1/autorizar-venda')
@api.expect(authorize_sale_model.AuthorizeSaleModel.get_model(api))
class AuthorizeSaleController(Resource):
    @api.doc(responses={
        201: 'CREATED',
        400: 'BAD_REQUEST',
        500: 'INTERNAL_SERVER_ERROR'
    })
    @api.marshal_with(response_model.ResponseModel.get_model(api), code=201,
                      description='Sale authorized successfully')
    def post(self):
        sale_service = AuthorizeSaleService()
        data = api.payload
        response = sale_service.autorizar_venda(data)
        return response, 201
