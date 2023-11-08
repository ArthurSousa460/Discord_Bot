import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content=True
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print("Estou pronto!")



@bot.command(name="test")
async def test(ctx):
    name = ctx.author.name

    response = "ola, " + name
    await ctx.send(response)



bot.run("MTE3MTg3MTQxNzM2OTkwNzMzMQ.GlNLKI.V7UNDJZRHpI28Yg8c8BS33Y89fxFV1FZLJUCac")