import os
import discord
from discord.ext import commands, tasks
import aiohttp
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} 봇이 준비되었습니다!')
    print(f'CHANNEL_ID: {os.getenv("CHANNEL_ID")}')
    bitcoin_price_task.start()

async def get_bitcoin_price():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,krw') as response:
            if response.status == 200:
                data = await response.json()
                usd_price = data['bitcoin']['usd']
                krw_price = data['bitcoin']['krw']
                return f'현재 비트코인 가격:\n${usd_price:,.2f} (USD)\n₩{krw_price:,.0f} (KRW)'
            else:
                return '죄송합니다. 현재 비트코인 가격을 가져올 수 없습니다.'

@tasks.loop(minutes=1)
async def bitcoin_price_task():
    print("bitcoin_price_task 실행 중...")
    channel_id = os.getenv('CHANNEL_ID')
    if channel_id:
        channel = bot.get_channel(int(channel_id))
        if channel:
            price_message = await get_bitcoin_price()
            await channel.send(price_message)
            print(f"메시지 전송 완료: {price_message}")
        else:
            print(f"채널을 찾을 수 없습니다. CHANNEL_ID: {channel_id}")
    else:
        print("CHANNEL_ID가 설정되지 않았습니다.")

@bitcoin_price_task.before_loop
async def before_bitcoin_price_task():
    await bot.wait_until_ready()
    print("bitcoin_price_task 시작 준비 완료")

@bot.command(name='start')
async def start_task(ctx):
    if not bitcoin_price_task.is_running():
        bitcoin_price_task.start()
        await ctx.send("비트코인 가격 알림을 시작합니다.")
    else:
        await ctx.send("이미 비트코인 가격 알림이 실행 중입니다.")

@bot.command(name='stop')
async def stop_task(ctx):
    if bitcoin_price_task.is_running():
        bitcoin_price_task.cancel()
        await ctx.send("비트코인 가격 알림을 중지합니다.")
    else:
        await ctx.send("비트코인 가격 알림이 실행 중이지 않습니다.")

# .env 파일에서 봇 토큰을 가져옵니다
bot.run(os.getenv('DISCORD_TOKEN'))