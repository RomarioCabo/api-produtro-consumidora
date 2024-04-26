from threading import Thread

from application import create_app
from domain.process_sale.sale_listener import SaleListener

app = create_app()


def start_rabbitmq_listener():
    with app.app_context():
        listener = SaleListener()
        listener.start_consuming()


if __name__ == '__main__':
    rabbitmq_thread = Thread(target=start_rabbitmq_listener)
    rabbitmq_thread.start()

    # Inicia o servidor Flask
    app.run(debug=False, use_reloader=False)
