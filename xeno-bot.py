import datetime
import discord
from discord.ext import commands, tasks; 

bot = commands.Bot("!");

@bot.event
async def on_ready():
    print("... Bom dia?!");
    current_time.start();



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

@bot.command(name = "calcular")
async def calculate_expression(ctx, expression):
    response = eval(expression);

    await ctx.send(str(response) + ", é isso?");

@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now();
    now = now.strftime("%d/%m/%Y às %H:%M");

    channel = bot.get_channel(0000000000000000);

    await channel.send("Data atual: " + now);

bot.run("000000kjsdfjs000000kask000");