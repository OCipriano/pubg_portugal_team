# 🤖 PUBG Discord Bot — Portugal Team 🇵🇹

![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Discord](https://img.shields.io/badge/discord.py-2.3.2-blueviolet)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

Bot oficial da comunidade Portugal Team no Discord desenvolvido em Python.
Inclui comandos de estatísticas, informações sobre armas e mapas, destaques de jogo, regras do servidor e mensagens automáticas de boas-vindas.

---

## 🚀 Funcionalidades

### 🎉 Mensagem de boas-vindas automática

- Quando um novo membro entra no servidor, recebe uma mensagem privada em embed com todas as regras e informações necessárias sobre o servidor.

### 📜 Regras do servidor

- O comando `/regras` mostra um embed formatado com todas as regras (visível apenas para quem executa o comando).

### 🎮 PUBG Player Stats

- O comando `/playerstat` permite consultar **estatísticas detalhadas** de jogadores do **PUBG** diretamente no Discord, com suporte a três modos diferentes:
  - **Ranked** → Estatísticas competitivas (classificatórias)  
  - **Temporada Atual** → Estatísticas apenas da temporada em vigor em Squad-FPP
  - **Lifetime** → Estatísticas globais acumuladas desde sempre  

- Este comando é totalmente interativo, usando **dropdowns** e **modals** para facilitar a pesquisa.

### 🔫 Armas

- O Comando `/weapons` mostra informações sobre armas do PUBG (dados armazenados em weapons.json).

### 🗺️ Mapas

- O comando `/mapas` lista todos os mapas disponíveis no PUBG.

### 🎥 Highlights

- O comando `/highlights` apresenta clipes e destaques.

### ⚡ Cache

- Sistema de cache (cache.py) para reduzir chamadas desnecessárias à API.

---

## 📁 Estrutura do Projeto

```
📂 bot/
	├── bot.py                 # Ficheiro principal do bot
	├── cache.py               # Gestão de cache para dados da API
	├── pubg_api.py            # Integração com a API PUBG
	├── mapas.json             # Dados sobre mapas
	├── commands/              # Diretório com comandos
	│   ├── armas.py
	│   ├── highlights.py
	│   ├── mapas.py
	│   ├── playerstat.py
	│   ├── regras.py
	│   └── weapons.json
	└── events/                # Diretório com eventos
		└── novo_membro.py     # Evento de boas-vindas com regras
```

---

## 🛠️ Instalação

1. **Clona o repositório** ou extrai o `.zip`

   ```bash
   git clone https://github.com/seu-username/bot-pubg.git
   cd bot-pubg
   ```

2. Cria um ambiente virtual (opcional mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   .\venv\Scripts\activate    # Windows
   ```

3. **Instala as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. Cria um ficheiro `.env` com as seguintes variáveis:

   ```env
   # ENDPOINTS DAS APIS DO PUBG
   PUBG_API_KEY=KEY
   PUBG_API_BASE=URL

   # DISCORD
   DISCORD_TOKEN=TOKEN_DO_TEU_BOT

   # CONFIGURAÇÕES DAS AUTORIZAÇÕES DO DISCORD
   ALLOWED_ROLES=0000000000000000000,0000000000000000000
   BOT_OWNER_ID=000000000000000000

   # ENDPOINT DA API DO PUBG REPORT
   PUBGREPORT_API_BASE=URL
   ```
   
   • PUBG_API_KEY = Key da API do pubg.
   • PUBG_API_BASE = Endpoint da API do pubg.
   • DISCORD_TOKEN = Token do teu bot.
   • ALLOWED_ROLES = Roles do discord autorizados a utilizar o comando `/mapaskey`.
   • BOT_OWNER_ID = ID do utilizador de discord autorizado a utilizar o comando `/mapaskey`.
   • PUBGREPORT_API_BASE = Endpoint da API do pubg report.
   

5. Configurar intents no Discord Developer Portal

- Ativar SERVER MEMBERS INTENT
- Ativar MESSAGE CONTENT INTENT (se necessário para mensagens de texto)

---

## ▶️ Execução

Para iniciar o bot:

   ```bash
   python3 bot.py
   ```

---

## 📜 Exemplo de saída dos comandos

### 🗺️ Mapas

   ```bash
   🗺️ Mapas Ativos (EU)
   Semana 2 • 20 Aug → 26 Aug
   
   Erangel | Taego | Vikendi | Rondo | Deston
   ```
   
### 🔫️ Weapons

   ```bash
   🔫 AKM (AR)
   
   Munição     Dano          Cadência
   7.62mm      47            0.100s

   Velocidade  Estabilidade  Alcance
   715 m/s     Moderada      100-400m
​
   🎯 Áreas de Dano
   ━━━━━━━━━━━━━━
   Cabeça: 117.5
   Peito: 47
   Estômago: 40
   ```
   
### 🎥 Highlights

   ```bash
   🎥 Highlights de icub_
   
   Últimos 5 eventos registados no PUBG Report:
   
   icub_ → Muemte
   Evento: Matou (teammate)
   Quando: Aug 21, 2025
   Ver Vídeo
   
   icub_ → Muemte
   Evento: Derrubou (teammate)
   Arma: Thompson
   Distância: 32 m
   Quando: Aug 21, 2025
   Ver Vídeo
   
   icub_ → TF_Mitra
   Evento: Derrubou (teammate)
   Arma: M24
   Distância: 187 m
   Quando: Aug 21, 2025
   Ver Vídeo
   
   st4ynice → icub_
   Evento: Foi derrubado (teammate)
   Arma: Berreta686
   Distância: 8 m
   Quando: Aug 21, 2025
   Ver Vídeo
   
   lOrdKowalski → icub
   Evento: Foi derrubado (teammate)
   Arma: BerylM762
   Distância: 24 m
   Quando: Aug 21, 2025
   Ver Vídeo
   ```
   
### 📊 Playerstat

   ```bash
   📊 Estatísticas de icub_ (Temporada atual)
​
   🏆 Placement Stats
   ━━━━━━━━━━━━━━━━━━
   Matches Played: 154
   Chicken Dinners: 9 (5.8% )
   Top 10s: 64 (41.6% )
   Time Survived: 31 h 21 min
​
   🔫 Kill Stats
   ━━━━━━━━━━━━━━━━━━
   Kills: 233
   Deaths: 148
   Headshots: 59 (25.3%)
   Assists: 73
   Revives: 83
   Team Kills: 1
   Knocked Enemies: 236
​
   📈 Average Stats
   ━━━━━━━━━━━━━━━━━━
   Avg Time Survived: 12 min
   Avg Damage: 244.4
   K/D: 1.57
   KDA: 2.07
​
   🎲 Miscellaneous Stats
   ━━━━━━━━━━━━━━━━━━
   Most Kills in a Match: 8
   Longest Kill: 417.00m
   Boosts Used: 339
   Heals Used: 298
   Suicides: 1
​
   🎥 Highlights
   ━━━━━━━━━━━━━━━━━━
   🔗 PUBG Report
   Open Highlights
​
   👥 Clan
   ━━━━━━━━━━━━━━━━━━
   Portugal_Team [PT]
   Level 20
   82 members
   ```

---

## ⚙️ Requisitos

- Python 3.11 ou superior
- Conta no [Discord Developer Portal](https://discord.com/developers/applications) para criar o bot
- Chaves de API do **PUBG** e **PUBG Report**
- Bibliotecas:
  - discord.py
  - python-dotenv
  - requests
  - aiohttp

---

## 🧪 Testado em

- Python 3.11
- Ubuntu 22.04 & Windows 10
- Servidor de testes criado no Discord com permissões completas para o bot

---

## 📌️ Notas Finais

- Se um utilizador tiver bloqueado DMs de membros do servidor, o bot não conseguirá enviar a mensagem de boas-vindas.
- É recomendável criar um canal de boas-vindas público como alternativa.
- O sistema de cache melhora a performance das consultas à API PUBG, mas pode ser limpo manualmente se necessário.

---

## 📬 Contribuição

- Para contribuir:
  - Faça um fork do repositório
  - Crie uma branch (git checkout -b minha-feature)
  - Commit as alterações (git commit -m "Adicionei nova feature")
  - Faça push (git push origin minha-feature)
  - Abra um Pull Request

---

## 📬 Contato

- Desenvolvido por **Cipriano** para o Servidor do Clan **Portugal Team** de PUBG
- Discord: PT Cipriano#8851
- Email: redealfa.password440@passmail.com
- Servidor Discord: 

---

## 🛡️ Licença

- Este projeto é open-source sob a licença MIT.
- Sinta-se à vontade para usar, modificar e contribuir.

---
