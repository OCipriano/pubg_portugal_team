import os
import sys
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Importar setups dos comandos
from commands.playerstat import setup_playerstat
from commands.armas import setup_armas
from commands.mapas import setup_mapas, setup_mapaskey
from commands.highlights import setup_highlights
from commands.regras import setup_regras
from events.novo_membro import setup_novo_membro

# Corrigir event loop apenas no Windows
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Carregar variáveis do .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Inicializar bot
intents = discord.Intents.default()
intents.message_content = False
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# Evento on_ready para sincronizar comandos
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    try:
        synced = await tree.sync()
        print(f"🔁 Comandos sincronizados: {len(synced)}")
    except Exception as e:
        print("Erro ao sincronizar comandos:", e)

# Adicionar comandos
setup_playerstat(bot)
setup_armas(bot)
setup_mapas(bot)
setup_mapaskey(bot)
setup_highlights(bot)
setup_novo_membro(bot)
setup_regras(bot)

# Iniciar o bot
bot.run(DISCORD_TOKEN)
