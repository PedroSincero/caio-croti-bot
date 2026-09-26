import os

import discord
from discord import app_commands

TOKEN = os.environ["DISCORD_TOKEN"]


class CaioBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Bot conectado como {self.user}")

        print("\nServidores conectados:")
        for guild in self.guilds:
            print(f"- {guild.name} | ID: {guild.id}")

        print("\nSincronizando comandos globais...")

        try:
            synced = await self.tree.sync()

            print(f"{len(synced)} comando(s) global(is) sincronizado(s):")

            for command in synced:
                print(f"- /{command.name}")

        except Exception as error:
            print(f"Erro ao sincronizar comandos: {error}")


bot = CaioBot()


@bot.tree.command(
    name="caiocroti",
    description="Calcula a pontuação do Caio Croti."
)
@app_commands.describe(
    points="Pontos recebidos."
)
async def caiocroti(
    interaction: discord.Interaction,
    points: int,
):
    if points <= 0:
        await interaction.response.send_message(
            "📊 Os pontos precisam ser maiores que 0."
        )
        return

    # Média de combate Caio Croti
    pontuacao = round(points / 42)

    # Determina a fase usando os pontos originais.
    # Cada fase possui 42 pontos.
    fase = min((points - 1) // 42 + 1, 10)

    # Mensagens provisórias
    mensagens = {
        1: (
            "**Level 1 de AVCaio Score**\n"
            "Condenem-me não me importa, a história me absolverá"
        ),
        2: (
            "**Level 2 de AVCaio Score**\n"
            "Estou buscando a melhora"
        ),
        3: (
            "**Level 3 de AVCaio Score🚀**\n"
        ),
        4: (
            "**Level 4 de AVCaio Score🚀**\n"
        ),
        5: (
            "**Level 5 de AVCaio Score 🚀**\n"
        ),
        6: (
            "*Level 6 de AVCaio Score 🔥**\n"
        ),
        7: (
            "**Level 7 de AVCaio Score 💀**\n"
        ),
        8: (
            "**Level 8 de AVCaio Score ⚡**\n"
        ),
        9: (
            "**Level 9 de AVC Score 👑**\n"
        ),
        10: (
            "Isso aqui já não pode ser considerado normal. Você ultrapassou todas as expectativas e entrou oficialmente na fora da curva caiolisticas."
        ),
    }

    mensagem = mensagens[fase]

    # Define a extensão da imagem.
    extensao = "jpg" if fase == 10 else "jpeg"

    # Caminho da imagem dentro do projeto.
    imagem_path = f"levels/{fase}.{extensao}"

    # Cria o embed.
    embed = discord.Embed(
        title=f"[TEST] 🏆 FASE {fase}",
        description=(
            f"📊 **Points recebidos:** {points}\n"
            f"⚔️ **Em média de combate Caio Croti:** "
            f"{pontuacao} pontos\n\n"
            f"{mensagem}"
        ),
    )

    # Adiciona a imagem como anexo do Discord.
    arquivo = discord.File(
        imagem_path,
        filename=f"level_{fase}.{extensao}"
    )

    embed.set_image(
        url=f"attachment://level_{fase}.{extensao}"
    )

    await interaction.response.send_message(
        embed=embed,
        file=arquivo,
    )


bot.run(TOKEN)