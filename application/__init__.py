from flask import Flask
from flask_restx import Api

from infrastructure.config.cache_config import CacheConfig


def create_app():
    app = Flask(__name__)

    cache_config = CacheConfig()

    cache_config.init_app(app)

    api = Api(app, version='1.0', title='API Autorizar venda',
              description='Uma API que autoriza as vendas')

    from .controller.authorize_sale_controller import api as sale_api
    api.add_namespace(sale_api)

    app.cache = cache_config.get_cache()

    return app
