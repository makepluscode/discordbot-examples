import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# .env 파일에서 환경 변수 로드
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'안녕하세요, {ctx.author.name}님!')

# .env 파일에서 봇 토큰을 가져옵니다
bot.run(os.getenv('DISCORD_TOKEN'))