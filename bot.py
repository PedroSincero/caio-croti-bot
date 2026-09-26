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

    # Média de combate AVCaio Score
    pontuacao = round(points / 42)

    # Determina o Level usando os Points originais.
    # Cada Level possui 42 Points.
    level = min((points - 1) // 42 + 1, 10)

    # Mensagens provisórias
    mensagens = {
        1: (
            "Condenem-me não me importa, a história me absolverá"
        ),
        2: (
            "Estou buscando a melhora"
        ),
        3: (
            "**3 de AVCaio Score🚀**\n"
        ),
        4: (
            "**4 de AVCaio Score🚀**\n"
        ),
        5: (
            "**5 de AVCaio Score 🚀**\n"
        ),
        6: (
            "*6 de AVCaio Score 🔥**\n"
        ),
        7: (
            "**7 de AVCaio Score 💀**\n"
        ),
        8: (
            "**8 de AVCaio Score ⚡**\n"
        ),
        9: (
            "**9 de AVC Score 👑**\n"
        ),
        10: (
            "Você ultrapassou todas as expectativas e entrou oficialmente "
            "na fora da curva caiolisticas."
        ),
    }

    mensagem = mensagens[level]

    # Define a extensão da imagem.
    extensao = "jpg" if level == 10 else "jpeg"

    # Caminho da imagem dentro do projeto.
    imagem_path = f"levels/{level}.{extensao}"

    # Cria o embed.
    embed = discord.Embed(
        title=f"🏆 Level {level}",
        description=(
            f"📊 **Points recebidos:** {points}\n"
            f"⚔️ **Média de combate AVCaio Score:** "
            f"{pontuacao} pontos\n\n"
            f"Ou seja, sua pontuação é equivalente a **{pontuacao}x AVG de Caio Score**.\n\n"
            f"{mensagem}"
        ),
    )

    # Adiciona a imagem como anexo do Discord.
    arquivo = discord.File(
        imagem_path,
        filename=f"level_{level}.{extensao}"
    )

    embed.set_image(
        url=f"attachment://level_{level}.{extensao}"
    )

    await interaction.response.send_message(
        embed=embed,
        file=arquivo,
    )


@bot.tree.command(
    name="tabela",
    description="Mostra a tabela de conversão do AVCaio Score."
)
async def tabela(
    interaction: discord.Interaction,
):
    embed = discord.Embed(
        title="📊 Tabela AVCaio Score",
        description=(
            "**Como funciona?**\n\n"
            "Os **Points** recebidos são divididos por **42** "
            "para calcular a **Média** de combate AVCaio Score.\n\n"
            "O resultado é arredondado para o número inteiro mais próximo.\n\n"
            "O **Level** é definido pela quantidade de Points recebidos. "
            "A partir de 399 Points, o usuário permanece no Level 10.\n\n"
            "**Fórmula:** `Points ÷ 42 = Média`"
        ),
    )

    tabela_texto = (
        "```text\n"
        " Points       Média       Level\n"
        "──────────────────────────────\n"
        " 1–62         0–1           1\n"
        " 63–104         2           2\n"
        " 105–146        3           3\n"
        " 147–188        4           4\n"
        " 189–230        5           5\n"
        " 231–272        6           6\n"
        " 273–314        7           7\n"
        " 315–356        8           8\n"
        " 357–398        9           9\n"
        " 399+          10+          10\n"
        "```"
    )

    embed.add_field(
        name="📈 Conversão",
        value=tabela_texto,
        inline=False,
    )

    embed.set_footer(
        text="AVCaio Score • Sistema de Levels"
    )

    await interaction.response.send_message(
        embed=embed
    )


bot.run(TOKEN)