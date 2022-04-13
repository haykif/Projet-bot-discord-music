# Importations
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from dotenv import load_dotenv
import os

#skldjfhsdfgs
# Crédits
load_dotenv('token.env')

# Préfix du bot: -
bot = commands.Bot(command_prefix='-')

# Montre à l'utilisateur que le bot est prêt à être utilisé
@bot.event 
async def on_ready(): 
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="DR.Dre Still"))
    print('Musicx est à votre service')

# Commande pour que le bot rejoigne le canal de l'utilisateur. Si le bot se trouve dans un canal différent autre que celui de l'utilisateur, il se déplacera vers le canal dans lequel se trouve l'utilisateur.
@bot.command(name='join', help='Fait rejoindre le bot au salon vocal⬅️')
async def join(ctx):
    salon = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(salon)
    else:
        voice = await salon.connect()

# Une commande du bot qui sert à jouer une musique depuis une URL Youtube
@bot.command(name='play', help='+<URL YouTube> Sert à jouer une musique ▶️')
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    son = get(bot.voice_clients, guild=ctx.guild)

    if not son.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        son.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        son.is_playing()
        await ctx.send('**Musique lancée, amusez-vous bien 😉**')

# Envoi d'un message en disant que le bot joue déjà une musique
    else:
        await ctx.send("Le bot joue déjà une morceau")
        return


# Une commande du bot qui sert à continuer de jouer la musique si cette dernière est en pause
@bot.command(name='resume', help='redémarre la musique mise en pause ⏯️')
async def resume(ctx):
    son = get(bot.voice_clients, guild=ctx.guild)

    if not son.is_playing():
        son.resume()
        await ctx.send("Musicx continue à jouer de là où il s'est arrêté")
    else:
        await ctx.send("Le bot ne jouait aucune musique. Utilisez donc la commande play pour commencer à écouter quelques morceaux.")


# Une commande du bot qui met en pause la musique en cours d'exécution
@bot.command(name='pause', help='Cette commande sert à mettre en pause la musique ⏸️')
async def pause(ctx):
    son = get(bot.voice_clients, guild=ctx.guild)

    if son.is_playing():
        son.pause()
        await ctx.send('Musicx a mis en pause la musique')

@bot.command(name='dc', help='Fait quitter le bot du salon vocal 🔌')
async def quit(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("Musicx n'est pas connecté à un salon vocal")

# Une commande qui sert à tout stopper
@bot.command(name='stop', help="Sert à tout stopper ⏹️")
async def stop(ctx):
    son = get(bot.voice_clients, guild=ctx.guild)

    if son.is_playing():
        son.stop()
        await ctx.send('Arrêt en cours...')


# Une commande qui sert à supprimer tout les messages d'un salon textuel
@bot.command(name='clear', help="Sert à supprimer tout les messages d'un salon textuel 🗑️")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Les messages viennent d'être supprimés")

# Commande démmarant le bot
if __name__ == "__main__" :
    bot.run(os.getenv('TOKEN'))