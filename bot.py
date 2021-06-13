import asyncio, discord, time, youtube_dl
from discord.ext import commands
import os


bot = commands.Bot(command_prefix='*')


#token = ""

# 봇이 구동되었을 때 보여지는 코드
@bot.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(bot.user.name)
    print(bot.user.id)
    print("================")

@bot.command()
async def 신고(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio('singo.mp3'), after=lambda e: print('done', e))

    while voice.is_playing():
    	time.sleep(.1)
        
    await voice.disconnect()
    
@bot.command()
async def 컷(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio('cut.mp3'), after=lambda e: print('done', e))

    while voice.is_playing():
    	time.sleep(.1)
        
    await voice.disconnect()

@bot.command()
async def 모자(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio('hat.mp3'), after=lambda e: print('done', e))

    while voice.is_playing():
    	time.sleep(.1)
        
    await voice.disconnect()

@bot.command()
async def p(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command()
async def l(ctx):
	await bot.voice_clients[0].disconnect()
    
# 봇이 특정 메세지를 받고 인식하는 코드
@bot.event
async def on_message(message):

    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None
    if '신고' in message.content:
        await message.channel.send(' 애쉬ㅣㅣㅣㅣ 신고할게 ~ ')
    if '애쉬' in message.content:
        await message.channel.send(' 애쉬ㅣㅣㅣㅣ 신고할게 ~ ')
    if '신' in message.content and '고' in message.content and not '신고' in message.content:
        await message.channel.send(' 애쉬ㅣㅣㅣㅣ 신고할게 ~ ')
    if message.content.startswith('!6렙'):
        for a in range(0,5):
            await message.channel.send(f"<@409684631403757570>" * 50)
    if message.content.startswith('!all'):
        for a in range(0,5):
            await message.channel.send(f"@everyone" * 50)
    if '*' in message.content:
        # another action codes ...
        await bot.process_commands(message)
        return

    
#bot.run(token)
bot.run(os.environ['token'])