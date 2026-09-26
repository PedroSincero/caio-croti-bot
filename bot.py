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

        try:
            synced = await self.tree.sync()
            print(f"{len(synced)} comando(s) sincronizado(s).")
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
    # Calcula a pontuação do Caio Croti
    pontuacao = round(points / 6)

    # Define a faixa usando os POINTS originais
    if 1 <= points <= 117:
        faixa = 1
        mensagem = "Você está na Faixa 1! 🟢"

    elif 118 <= points <= 233:
        faixa = 2
        mensagem = "Você está na Faixa 2! 🔵"

    elif 234 <= points <= 350:
        faixa = 3
        mensagem = "Você está na Faixa 3! 🟣"

    elif 351 <= points <= 466:
        faixa = 4
        mensagem = "Você está na Faixa 4! 🟠"

    elif points >= 467:
        faixa = 5
        mensagem = "Você está na Faixa 5! 🏆"

    else:
        faixa = None
        mensagem = "Os pontos precisam ser maiores que 0."

    if faixa is not None:
        await interaction.response.send_message(
            f"Points recebidos: **{points}**\n"
            f"Pontuação Caio Croti: **{pontuacao}**\n"
            f"Faixa: **{faixa}**\n\n"
            f"{mensagem}"
        )
    else:
        await interaction.response.send_message(
            f"Points recebidos: **{points}**\n"
            f"Pontuação Caio Croti: **{pontuacao}**\n\n"
            f"{mensagem}"
        )