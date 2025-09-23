# ================================================================================ #
#                                                                                  #
# Ficheiro:      pubg_api.py                                                       #
# Autor:         NunchuckCoder                                                     #
# Versão:        1.0                                                               #
# Data:          Julho 2025                                                        #
# Descrição:     Funções assíncronas para interagir com a API PUBG.                #
#                Permite obter informações de jogadores, estatísticas, clãs,       #
#                temporadas e rankings. Inclui tratamento de erros e logs básicos. #
# Licença:       MIT License                                                       #
#                                                                                  #
# ================================================================================ #

import os
import aiohttp
from dotenv import load_dotenv

# ================================================================================ #
# ------------------------ CARREGAR VARIÁVEIS DE AMBIENTE ------------------------ #
# ================================================================================ #

load_dotenv()

# Chave da API PUBG (obrigatória)
PUBG_API_KEY = os.getenv("PUBG_API_KEY")
if not PUBG_API_KEY:
    raise RuntimeError("PUBG_API_KEY não definida (ver .env).")

# Base da API PUBG
PUBG_API_BASE = os.getenv("PUBG_API_BASE")
if not PUBG_API_BASE:
    raise RuntimeError("PUBG_API_BASE não definida (ver .env).")
    
# Cabeçalhos usados em todos os requests
HEADERS = {
    "Authorization": f"Bearer {PUBG_API_KEY}",
    "Accept": "application/vnd.api+json"
}

# ================================================================================ #
# ------------------------------ FUNÇÕES DE JOGADOR ------------------------------ #
# ================================================================================ #

async def get_player_id(session, username):
    """
    Obtém o ID PUBG de um jogador a partir do nome.
    Retorna None se não for encontrado.
    """
    url = f"{PUBG_API_BASE}/shards/steam/players?filter[playerNames]={username}"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            print(f"[ERRO] {resp.status} ao obter ID do jogador: {await resp.text()}")
            return None, None
        data = await resp.json()
        if not data.get("data"):
            return None, None

        player_data = data["data"][0]
        return player_data["id"], player_data["attributes"]["name"]


async def get_player_data(session, shard, player_id):
    """
    Busca dados detalhados de um jogador (perfil).
    """
    url = f"{PUBG_API_BASE}/shards/{shard}/players/{player_id}"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            print(f"[ERRO] Status {resp.status} ao buscar dados do jogador")
            return None
        return await resp.json()

# ================================================================================ #
# ----------------------------- FUNÇÕES DE TEMPORADA ----------------------------- #
# ================================================================================ #

async def get_current_season(session):
    """
    Retorna o ID da temporada atual (se existir).
    """
    url = f"{PUBG_API_BASE}/shards/steam/seasons"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            return None
        data = await resp.json()
        for season in data.get("data", []):
            if season.get("attributes", {}).get("isCurrentSeason"):
                return season.get("id")
    return None

# ================================================================================ #
# --------------------------- FUNÇÕES DE ESTATÍSTICAS ---------------------------- #
# ================================================================================ #

async def get_player_stats(session, player_id, season_id, stat_type="normal"):
    """
    Obtém estatísticas normais do jogador (ex: squad-fpp).
    Por default retorna stats normais da temporada atual.
    """
    url = f"{PUBG_API_BASE}/shards/steam/players/{player_id}/seasons/{season_id}"
    async with session.get(url, headers=HEADERS) as response:
        if response.status != 200:
            print(f"[ERRO] Status {response.status} ao buscar stats: {await response.text()}")
            return None

        data = await response.json()
        stats = data.get("data", {}).get("attributes", {}).get("gameModeStats", {})

        if stat_type == "normal":
            return stats.get("squad-fpp") or {}
        return None


async def get_ranked_stats(session, player_id, season_id):
    """
    Obtém estatísticas ranqueadas do jogador (squad-fpp).
    """
    url = f"{PUBG_API_BASE}/shards/steam/players/{player_id}/seasons/{season_id}/ranked"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            return None
        data = await resp.json()
        return data.get("data", {}).get("attributes", {}).get("rankedGameModeStats", {}).get("squad-fpp", {})

async def get_lifetime_stats(session, player_id):
    """
    Obtém estatísticas lifetime do jogador (squad-fpp).
    """
    url = f"{PUBG_API_BASE}/shards/steam/players/{player_id}/seasons/lifetime"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            print(f"[ERRO] Status {resp.status} ao buscar lifetime stats: {await resp.text()}")
            return None

        data = await resp.json()
        stats = data.get("data", {}).get("attributes", {}).get("gameModeStats", {})
        return stats.get("squad-fpp") or {}

# ================================================================================ #
# ------------------------------- FUNÇÕES DE CLÃS -------------------------------- #
# ================================================================================ #

async def get_clan_info(session, player_id):
    """
    Busca informações do clã de um jogador.
    Faz duas chamadas:
      1. Busca o clanId do jogador
      2. Busca os dados detalhados do clã
    """
    # 1ª chamada -> dados do jogador
    url = f"{PUBG_API_BASE}/shards/steam/players/{player_id}"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            print(f"[ERRO] ao obter dados do jogador: {resp.status}")
            return None

        player_data = await resp.json()
        clan_id = player_data.get("data", {}).get("attributes", {}).get("clanId")
        if not clan_id:
            return None

    # 2ª chamada -> dados do clã
    url = f"{PUBG_API_BASE}/shards/steam/clans/{clan_id}"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            print(f"[ERRO] ao obter dados do clã: {resp.status}")
            return None

        clan_data = await resp.json()
        return clan_data.get("data", {}).get("attributes", None)


async def get_clan_data_online(session, clan_id):
    """
    Busca dados de um clã diretamente pelo clan_id.
    """
    url = f"{PUBG_API_BASE}/shards/steam/clans/{clan_id}"
    async with session.get(url, headers=HEADERS) as resp:
        if resp.status != 200:
            print(f"[ERRO] Status {resp.status} ao buscar dados do clã")
            return None
        return await resp.json()
