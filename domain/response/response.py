class Response:
    def __init__(self, status, timestamp):
        self.status = status
        self.timestamp = timestamp

    def __str__(self):
        return f"Response(status={self.status}, timestamp={self.timestamp})"
