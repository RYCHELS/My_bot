import discord
import random
import os
import requests
from discord.ext import commands
from bot_logic import genn_pass

# Membaca token dari file token.txt
with open("Token.txt", "r") as f:
    token = f.read().strip()

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passw(ctx, panjang=5):
    await ctx.send(genn_pass(panjang))

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx, category: str = None):
    if category:
        folder_path = f'Pictures/{category}'
    else:
        folder_path = 'Pictures'

    if not os.path.exists(folder_path) or not os.listdir(folder_path):
        await ctx.send("Kategori tidak ditemukan atau folder kosong!")
        return

    img_name = random.choice(os.listdir(folder_path))
    with open(f'{folder_path}/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command(name='duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(token)
