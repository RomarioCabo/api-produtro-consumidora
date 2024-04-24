import pika


class RabbitMQConfig:
    def __init__(self, queue_name="autorizar-venda-queue", exchange_name="autorizar-venda-queue-exchange",
                 routing_key="autorizar-venda-queue-routing-json-key", host="localhost", port=5672, username="guest",
                 password="guest", virtual_host="/"):
        self.queue_name = queue_name
        self.exchange_name = exchange_name
        self.routing_key = routing_key
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.virtual_host = virtual_host

    def create_connection(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        parameters = pika.ConnectionParameters(host=self.host, port=self.port, virtual_host=self.virtual_host,
                                               credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        return connection, channel

    def declare_queue(self, channel):
        channel.queue_declare(queue=self.queue_name, durable=True)

    def declare_exchange(self, channel):
        channel.exchange_declare(exchange=self.exchange_name, exchange_type='topic')

    def bind_queue(self, channel):
        channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key=self.routing_key)

    def setup(self):
        connection, channel = self.create_connection()
        self.declare_queue(channel)
        self.declare_exchange(channel)
        self.bind_queue(channel)
        connection.close()
