# ================================================================================ #
#                                                                                  #
# Ficheiro:      bot.py                                                            #
# Autor:         NunchuckCoder                                                     #
# Versão:        1.0                                                               #
# Data:          Julho 2025                                                        #
# Descrição:     Bot para Discord com comandos de estatísticas, mapas, armas,      #
#                destaques e regras, além de gestão de novos membros. Inclui       #
#                sincronização automática de comandos e suporte a múltiplos        #
#                eventos.                                                          #
# Licença:       MIT License                                                       #
#                                                                                  #
# ================================================================================ #
#                                                                                  #
# Funcionalidades principais:                                                      #
#   1. /regras       - Regras do servidor                                          #
#   2. /playerstat   - Estatísticas no modo Ranked, Temporada Atual e Lifetime     #
#   3. /weapons      - Informações sobre as armas existentes no jogo               #
#   4. /mapas        - Mapas (EU) que estão ativos na semana                       #
#   5. /highlights   - Vê os teus highlights captados por streamers na Twitch      #
#   7. Boas vindas   - Gestão de novos membros e notificações                      #
#                                                                                  #
# ================================================================================ #

import os
import sys
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# ================================================================================ #
# ------------------------- IMPORTAR SETUPS DOS COMANDOS ------------------------- #
# ================================================================================ #
from commands.playerstat import setup_playerstat
from commands.armas import setup_armas
from commands.mapas import setup_mapas, setup_mapaskey
from commands.highlights import setup_highlights
from commands.regras import setup_regras
from events.novo_membro import setup_novo_membro

# ================================================================================ #
# --------------------- CORRIGIR EVENT LOOP APENAS NO WINDOWS -------------------- #
# ================================================================================ #

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# ================================================================================ #
# ------------------------ CARREGAR VARIÁVEIS DE AMBIENTE ------------------------ #
# ================================================================================ #

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# ================================================================================ #
# -------------------------------- INICIALIZAR BOT ------------------------------- #
# ================================================================================ #

intents = discord.Intents.default()
intents.message_content = False
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# ================================================================================ #
# ------------------------------ SINCRONIZAR COMANDOS ---------------------------- #
# ================================================================================ #

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    try:
        synced = await tree.sync()
        print(f"🔁 Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print("Erro ao sincronizar comandos:", e)

# ================================================================================ #
# ------------------------------- ADICIONAR COMANDOS ----------------------------- #
# ================================================================================ #

setup_playerstat(bot)
setup_armas(bot)
setup_mapas(bot)
setup_mapaskey(bot)
setup_highlights(bot)
setup_novo_membro(bot)
setup_regras(bot)

# ================================================================================ #
# ---------------------------------- INICIAR BOT --------------------------------- #
# ================================================================================ #

bot.run(DISCORD_TOKEN)
