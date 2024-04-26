from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Inicializa SQLAlchemy sem um app


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sales_user:sales_password@192.168.0.9:5442/sales-db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)  # Associa o db ao app Flask

    with app.app_context():
        db.create_all()  # Cria as tabelas se não existirem

    api = Api(app, version='1.0', title='API Autorizar Venda',
              description='Uma API que autoriza as vendas')

    from .controller.authorize_sale_controller import api as sale_api
    api.add_namespace(sale_api)

    return app
