import discord
from discord.ext import commands; 

bot = commands.Bot("!");

@bot.event
async def on_ready():
    print("... Bom dia?!");

# @bot.event
# async def on_message():
    # if message.author == bot.user:
      # return;
     # await bot.process_commands(message);


@bot.command(name = "comandos")
async def send_command(ctx):
    name = ctx.author.name;
    response = "Ainda estou em desenvolvimento, não faço muita coisa além de dar 'Oi'.";
    await ctx.send(response);

@bot.command(name = "oi")
async def send_hello(ctx):
    name = ctx.author.name;
    response = "Fala pra mim, " + name;
    await ctx.send(response);

bot.run("OTgxNjIwMDI5OTAyNzAwNTk0.GqBf51.zrGh9gs8VFiXf8PBIOunbv1JA3zOYpNSoyFdIo");