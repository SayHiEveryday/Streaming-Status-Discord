import os
try:
    import discord
    from discord.ext.commands import Bot
    from discord.ext import commands
    import time
except ImportError:
    print("seem like you didn't install some module yet \n we will install for you please wait patiently")
    os.system("python -m pip install discord")
    os.system("python -m pip install config")
    os.system("python -m pip install time")
except:
    pass

bot = commands.Bot(help_command=None , selfbot=True , command_prefix=None)

d = discord
token = input("your token: ")
name = input("name: ")
url = input("Your Twitch url: ")
status = input("Status (online , dnd , idle , offline): ")

print("Thanks for using my basic streaming")

if status == 'online':
    statuss = d.Status.online
elif status == 'dnd':
    statuss = d.Status.dnd
elif status == 'idle':
    statuss = d.Status.idle
elif status == 'offline':
    statuss = d.Status.online
    print("you enter offline which will not working , i will set it as online")

@bot.event
async def on_ready():
    activity = d.Streaming(name=name , url=url)
    await bot.change_presence(status=statuss , activity=activity)
    print(f"Done! Right now you are login as {bot.user}")

bot.run(token)