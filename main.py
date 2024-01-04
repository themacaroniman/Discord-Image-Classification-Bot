import discord
from discord.ext import commands
from model import get_class 

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
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f"./{file_name}")
            await ctx.send(f'file telah disimpan di=./{file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)
            
            if hasil[0] == 'INDONESIA\n' and hasil[1] >= 0.6:
                await ctx.send('Ini adalah bendera Indonesia')
                await ctx.send('Negara ini terletak di Benua Asia')
            elif hasil[0] == 'MONACO\n' and hasil[1] >=  0.6:
                await ctx.send('Ini adalah bendera Monako')
                await ctx.send('Negara ini terletak di Benua Eropa')
            else: 
                await ctx.send('GAMBAR TIDAK VALID')
    else:
        await ctx.send('TIDAK ADA FILE YAND DIKIRIM')

bot.run("MTEyODk4NzQ5Njk1NzYxNjIxOQ.GmDLqU.lxCMf7l_cEyLz__gzbZg-NuGgEPoF5CMGeSC0s")
