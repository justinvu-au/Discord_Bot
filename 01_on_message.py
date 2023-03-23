import discord

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print('Bot is now online and ready to roll')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'Adri':
        await message.channel.send('Faster')

    else:
        await message.channel.send("Yo")

client.run('MTA4ODI5NjM1ODc5ODE2NDAzMA.GSr3Ua.-4WqPy2EiXrWvoFhn-Dp7intLfjhLc9gZONriE')
