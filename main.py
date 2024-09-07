import discord
from discord.ext import commands
from model import model_keras

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents) 
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def kontrol(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            fileName = attachment.filename
            fileUrl = attachment.url
            await ctx.send("Gönderdiğiniz fotoğrafı Kayıt Ettik! Yapay Zekaya Yüklüyoruz...")
            await ctx.send(model_keras(modelyolu='keras_model.h5', labelyolu='labels.txt', gorselyolu=f'{fileName}'))
            await ctx.send('Daha çok bilgi için bu siteyi ziyaret edin:https://muhti.pythonanywhere.com/')

bot.run("MTI3OTAyMTE4OTgzODI3ODY5Ng.GmpPgc.OPjDUrbGxmQygwhcCN4jIYTfjZIkpz03ealKWU")