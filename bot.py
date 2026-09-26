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
    name="caiocrotch",
    description="Calcula a pontuação do Caio Croti."
)
@app_commands.describe(
    valor="Valor que será dividido por 6."
)
async def caiocrotch(
    interaction: discord.Interaction,
    valor: int,
):
    pontuacao = round(valor / 6)

    await interaction.response.send_message(
        f"Valor recebido: **{valor}**\n"
        f"Pontuação Caio Croti: **{pontuacao}**"
    )


bot.run(TOKEN)