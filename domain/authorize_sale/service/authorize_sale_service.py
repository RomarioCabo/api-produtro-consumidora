import logging
from datetime import datetime
from pika.exceptions import AMQPConnectionError

from domain.response.response import Response
from infrastructure.config.rabbit_mq_config import RabbitMQConfig

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AuthorizeSaleService:
    def __init__(self):
        self.rabbit_config = RabbitMQConfig()
        self.rabbit_config.setup()  # Garantir que a configuração está completa
        self.exchange = self.rabbit_config.exchange_name
        self.routing_key = self.rabbit_config.routing_key

    def autorizar_venda(self, mensagem):
        if not mensagem:
            logging.error("Mensagem para autorização de venda está vazia.")
            return Response("MENSAGEM_VAZIA", datetime.now())

        try:
            with self.rabbit_config.create_connection() as (channel):
                logging.info(f"Enviando para fila {self.rabbit_config.queue_name} a mensagem: {mensagem}")
                channel.basic_publish(exchange=self.exchange,
                                      routing_key=self.routing_key,
                                      body=str(mensagem))
            return Response("EM_PROCESSAMENTO", datetime.now())
        except AMQPConnectionError as e:
            logging.error("Failed to connect to RabbitMQ server: %s", e)
            return Response("FALHA_DE_CONEXAO", datetime.now())
