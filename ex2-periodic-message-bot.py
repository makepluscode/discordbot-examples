import os
import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

# .env 파일에서 환경 변수 로드
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 봇이 준비되었습니다!')
    send_periodic_message.start()

@bot.command(name='안녕')
async def hello(ctx):
    await ctx.send(f'안녕하세요, {ctx.author.name}님!')

@bot.command(name='정보')
async def info(ctx):
    await ctx.send('저는 Python으로 만들어진 간단한 Discord 봇입니다.')

@tasks.loop(minutes=1)  # 1분마다 실행
async def send_periodic_message():
    channel = bot.get_channel(int(os.getenv('CHANNEL_ID')))  # 메시지를 보낼 채널 ID
    if channel:
        await channel.send("안녕하세요! 1분마다 보내는 정기적인 메시지입니다.")

@send_periodic_message.before_loop
async def before_send_periodic_message():
    await bot.wait_until_ready()  # 봇이 준비될 때까지 기다립니다.

# .env 파일에서 봇 토큰을 가져옵니다
bot.run(os.getenv('DISCORD_TOKEN'))