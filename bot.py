import discord
from discord.ext import commands

TOKEN = 'NDg1OTM1NjUzODcyMjA1ODc2.Dm3ydw.AiIoH4PeB7K8045kEGvSv4xugMA'
BOT_PREFIX = "!"

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.command(name = 'hello',
                description = 'Says hello to user',
                pass_context = True)
async def hello(context):
    await client.say("Hello " + context.message.author.mention + "!")

client.remove_command('help')

@client.command(name='help',pass_context=True)
async def help(context):
    embed = discord.Embed(title = 'UC InHouse Bot',
                            description = 'Runs InHouses for the following games',
                            color = 0xe00122)
    embed.add_field(name = 'Supported Games', value='League of Legends, Rocket League', inline=False)
    embed.add_field(name='Bot maintained by',value='<@123627814166593538>')
    await client.say(embed=embed)


@client.command(name='queue',
                aliases = ['q'],
                pass_context = True)
# async def queue(context):


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
