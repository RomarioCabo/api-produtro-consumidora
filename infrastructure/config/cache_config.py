from flask_caching import Cache


class CacheConfig:
    _instance = None

    def __new__(cls, app=None):
        if not cls._instance:
            cls._instance = super(CacheConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self, app=None):
        if not hasattr(self, 'initialized'):
            self.cache = None
            self.app = app
            if app is not None:
                self.init_app(app)
            self.initialized = True

    def init_app(self, app):
        cache_config = {
            'CACHE_TYPE': 'redis',
            'CACHE_REDIS_URL': 'redis://my-redis:6379/0'
        }
        app.config.update(cache_config)
        self.cache = Cache(app)

    def get_cache(self):
        return self.cache
