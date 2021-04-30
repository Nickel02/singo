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

