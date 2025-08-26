import time

# =========================
# CLASSE DE CACHE (MEMÓRIA TEMPORÁRIA)
# =========================
# Esta classe implementa um sistema de cache simples em memória.
# Útil para evitar chamadas repetidas à API em curtos intervalos de tempo.
# Cada entrada tem um tempo de vida (TTL - Time To Live).
# =========================

class Cache:
    def __init__(self, ttl=300):
        """
        Inicializa a cache.
        :param ttl: Tempo de vida em segundos para cada item (default = 300s).
        """
        self.ttl = ttl              # TTL em segundos
        self.data = {}              # Dicionário que armazena os dados {key: (valor, expiração)}

    # =========================
    # OBTÉM UM ITEM DA CACHE
    # =========================
    def get(self, key):
        """
        Obtém um valor da cache, se ainda for válido.
        :param key: Chave do item.
        :return: Valor armazenado ou None se não existir/expirar.
        """
        if key in self.data:
            value, expiry = self.data[key]
            # Se ainda não expirou → retorna o valor
            if time.time() < expiry:
                return value
            else:
                # Expirado → remove da cache
                del self.data[key]
        return None

    # =========================
    # DEFINE/ATUALIZA UM ITEM NA CACHE
    # =========================
    def set(self, key, value):
        """
        Guarda um item na cache com tempo de expiração.
        :param key: Chave única.
        :param value: Valor a armazenar.
        """
        expiry = time.time() + self.ttl
        self.data[key] = (value, expiry)
