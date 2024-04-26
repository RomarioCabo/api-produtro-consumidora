from sqlalchemy.exc import SQLAlchemyError

from application import db


class SaleRepository:
    @staticmethod
    def save(new_sale):
        try:
            db.session.add(new_sale)
            db.session.commit()

            print("Venda salva com sucesso")
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Erro ao inserir a venda: {e}")
