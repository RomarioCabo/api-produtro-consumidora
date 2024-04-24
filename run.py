from application import create_app
from threading import Thread
from domain.process_sale.sale_listener import SaleListener

app = create_app()


def start_rabbitmq_listener():
    listener = SaleListener()
    listener.start_consuming()


if __name__ == '__main__':
    # Inicia o consumidor RabbitMQ em uma thread separada
    rabbitmq_thread = Thread(target=start_rabbitmq_listener)
    rabbitmq_thread.start()

    # Inicia o servidor Flask
    app.run(debug=True, use_reloader=False)  # Desative o reloader para evitar problemas com threads
