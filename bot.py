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
    pontuacao = round(points / 6)

    if 1 <= points <= 117:
        faixa = 1
        mensagem = (
            "[TEST] **NEON⚡**\n"
            "Você tem pontos equivalentes a Neon do Caio \n"
            "Ainda há muito chão pela frente, mas pelo menos você está tentando."
        )

    elif 118 <= points <= 233:
        faixa = 2
        mensagem = (
            "[TEST] **RAZE💥**\n"
            "Você está ao menos esta fazendo o entry — embora ninguém saiba exatamente qual era o seu plano.\n"
        )

    elif 234 <= points <= 350:
        faixa = 3
        mensagem = (
            "[TEST] **SOVA 🏹**\n"
            "Você chegou naquele nível em que escolhe Sova... \n"
            "Flecha? Drone? Revelação? Nada disso.\n"
            "**É só bala.**"
        )

    elif 351 <= points <= 466:
        faixa = 4
        mensagem = (
            "[TEST] **SKYE 🦅**\n"
            "Você já não está simplesmente jogando. Você está fazendo historia carregando o caio.\n"
            "**O time agradece, suas costas não.**"
        )

    elif points >= 467:
        faixa = 5
        mensagem = (
            "[TEST] **FORA DA CURVA 🚀**\n"
            "Isso aqui já não pode ser considerado normal.\n"
            "Você ultrapassou todas as expectativas e entrou oficialmente na fora da curva caiolisticas.\n"
        )

    else:
        faixa = None
        mensagem = "[TEST] Os pontos precisam ser maiores que 0."

    if faixa is not None:
        await interaction.response.send_message(
            f"[TEST] 📊 **Points recebidos:** {points}\n"
            f"[TEST] ⚔️ **Em média de combate Caio Croti:** "
            f"{pontuacao} pontos\n\n"
            f"[TEST] 🏆 **FAIXA {faixa}**\n\n"
            f"{mensagem}"
        )
    else:
        await interaction.response.send_message(
            f"[TEST] 📊 **Points recebidos:** {points}\n"
            f"[TEST] ⚔️ **Em média de combate Caio Croti:** "
            f"{pontuacao} pontos\n\n"
            f"{mensagem}"
        )


bot.run(TOKEN)