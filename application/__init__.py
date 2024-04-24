from flask import Flask
from flask_restx import Api


def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='API Autorizar venda',
              description='Uma API que autoriza as vendas')

    from .controller.authorize_sale_controller import api as sale_api
    api.add_namespace(sale_api)

    return app
