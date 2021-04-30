<<<<<<< HEAD
import discord
import asyncio

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "ODM3MzI2NDU2MTY5OTU1Mzc0.YIq7Bw.oybBiLZ1TBIXicUuan_nPmvWOcE"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    channel = message.channel
    user = message.author
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if '신고' in message.content:
        await channel.send(' 애쉬ㅣㅣㅣㅣ 신고할게 ~ ')
    if '애쉬' in message.content:
        await channel.send(' 애쉬ㅣㅣㅣㅣ 신고할게 ~ ')
    if '신' in message.content and '고' in message.content and not '신고' in message.content:
        await channel.send(' 애쉬ㅣㅣㅣㅣ 신고할게 ~ ')
    if message.content == '21만':
        await channel.send(' 21만? 애쉬ㅣㅣㅣㅣ 신고할게 ')
    if message.content == '신고할게1':
        await channel.send(f'{user.mention} 애쉬ㅣㅣㅣㅣ 신고할게 ~')
    if message.content.startswith('!6렙'):
        for a in range(0,5):
            await channel.send(f"<@409684631403757570>" * 50)

    

client.run(token)
=======
import discord, asyncio

app = discord.Client()

token = "ODM3MzI2NDU2MTY5OTU1Mzc0.YIq7Bw.ogaXTAMlbYu5w9kvuy5cBYdI4FY"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == '신고':
        await message.channel.send('애쉬 신고할게')

app.run(token)

>>>>>>> 36caf94ffb767b06709bb015ada86693e0933467
