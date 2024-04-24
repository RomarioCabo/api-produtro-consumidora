from infrastructure.config.cache_config import CacheConfig
from infrastructure.provider.tributario_client import TributarioClient


class TributoCacheService:
    def __init__(self):
        self.tributo_service = TributarioClient()
        self.cache = CacheConfig().get_cache()

    def consultar_com_cache(self, sku):
        @self.cache.cached(timeout=300, key_prefix='consulta-tributo')
        def consulta():
            return self.tributo_service.consultar_tributo(sku)

        return consulta()
