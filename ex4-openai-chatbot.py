import os
import discord
from discord.ext import commands
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

# Discord 봇 설정
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# OpenAI 클라이언트 설정
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# 지정된 채널 ID
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

@bot.event
async def on_ready():
    print(f'{bot.user} 봇이 준비되었습니다!')
    print(f'지정된 채널 ID: {CHANNEL_ID}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id != CHANNEL_ID:
        return

    if message.content.startswith('!chat'):
        await chat(message)

async def chat(message):
    try:
        # '!chat ' 이후의 메시지만 추출
        user_message = message.content[6:].strip()
        
        if not user_message:
            await message.channel.send("메시지를 입력해주세요. 예: !chat 안녕하세요")
            return

        print(f"받은 메시지: {user_message}")  # 디버깅을 위한 출력

        # OpenAI API를 사용하여 응답 생성
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        
        # 생성된 응답 추출
        ai_response = response.choices[0].message.content
        
        print(f"AI 응답: {ai_response}")  # 디버깅을 위한 출력
        
        # Discord에 응답 전송
        await message.channel.send(ai_response)
    except Exception as e:
        print(f"Error: {e}")
        await message.channel.send("죄송합니다. 응답을 생성하는 중 오류가 발생했습니다.")

# Discord 봇 실행
bot.run(os.getenv('DISCORD_TOKEN'))