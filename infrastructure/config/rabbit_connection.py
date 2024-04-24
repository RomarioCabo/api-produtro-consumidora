import pika
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class RabbitConnection:
    def __init__(self, parameters):
        self.parameters = parameters
        self.connection = None
        self.channel = None

    def __enter__(self):
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        return self.channel

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if self.channel:
                self.channel.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            logging.error("Failed to close RabbitMQ connection or channel: %s", e)
            raise
