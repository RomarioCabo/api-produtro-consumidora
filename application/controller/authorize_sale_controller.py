from flask import Flask
from flask_restx import Resource, Api

from domain.authorize_sale.model import authorize_sale_model, response_model
from domain.authorize_sale.service.authorize_sale_service import AuthorizeSaleService

app = Flask(__name__)
api = Api(app, version='1.0', title='API Autorizar venda',
          description='Uma API que autoriza as vendas')


@api.route('/api/v1/autorizar-venda')
@api.expect(authorize_sale_model.AuthorizeSaleModel.get_model(api))
class SendController(Resource):
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


if __name__ == '__main__':
    app.run(debug=True)
