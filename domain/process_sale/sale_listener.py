import logging
import time
from infrastructure.config.rabbit_mq_config import RabbitMQConfig
from pika.exceptions import AMQPConnectionError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SaleListener:
    def __init__(self):
        self.rabbit_config = RabbitMQConfig()

    def processar_venda(self, channel, method, properties, body):
        logging.info(f"Recebida mensagem para processamento: {body}")
        # Aqui você pode adicionar lógica para processar a venda.

        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        while True:
            try:
                with self.rabbit_config.create_connection() as channel:
                    channel.basic_qos(prefetch_count=1)
                    channel.basic_consume(queue=self.rabbit_config.queue_name, on_message_callback=self.processar_venda)

                    logging.info('Iniciando o consumo de mensagens.')
                    channel.start_consuming()
            except AMQPConnectionError as e:
                logging.error(f"Falha ao conectar com o servidor RabbitMQ: {e}")
                logging.info("Tentando reconectar em 5 segundos...")
                time.sleep(5)
            except Exception as e:
                logging.error(f"Erro inesperado: {e}")
                break
