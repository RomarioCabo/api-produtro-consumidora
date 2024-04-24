import logging
import time

from domain.sefaz.sefaz_service import SefazService
from infrastructure.config.rabbit_mq_config import RabbitMQConfig
from pika.exceptions import AMQPConnectionError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class VendaListener:
    def __init__(self):
        self.rabbit_config = RabbitMQConfig()
        self.sefaz_service = SefazService()

    def processar_venda(self, channel, method, properties, body):
        logging.info(f"Recebida mensagem para processamento: {body}")
        produtos = self.sefaz_service.gerar_produto(body)
        logging.info(f"PRODUTOS: {produtos}")

        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consuming(self):
        connection, channel = None, None
        while True:
            try:
                connection, channel = self.rabbit_config.create_connection()
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
            finally:
                if connection:
                    connection.close()
                    logging.info("Conexão com RabbitMQ fechada.")
