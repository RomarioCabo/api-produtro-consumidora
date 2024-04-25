import logging
import json
import time

from domain.sefaz.sefaz_service import SefazService
from infrastructure.config.rabbit_mq_config import RabbitMQConfig
from pika.exceptions import AMQPConnectionError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SaleListener:
    def __init__(self):
        self.rabbit_config = RabbitMQConfig()
        self.sefaz_service = SefazService()

    def processar_venda(self, channel, method, properties, body):
        try:
            mensagem_json = body.decode('utf-8')
            logging.info(f"Recebida mensagem para processamento: {mensagem_json}")

            mensagem_decodificada = json.loads(mensagem_json)

            produtos = self.sefaz_service.gerar_produtos(mensagem_decodificada)
            logging.info(f"Produtos: {produtos}")

        except json.JSONDecodeError as e:
            logging.error(f"Erro ao decodificar JSON: {e}")
            channel.basic_nack(delivery_tag=method.delivery_tag)
            return
        except UnicodeDecodeError as e:
            logging.error(f"Erro de codificação ao decodificar a mensagem: {e}")
            channel.basic_nack(delivery_tag=method.delivery_tag)
            return

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
