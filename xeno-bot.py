import requests
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
async def calculate_expression(ctx,*expression):
    expression = "".join(expression);
    response = eval(expression);

    await ctx.send(str(response) + ", é isso?");

@bot.command(name = "moeda")
async def binance(ctx, coin, base):
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}");
        data = response.json();
        price = data.get("price");

        if price:
            await ctx.send(f"Aqui a bosta : {coin}/{base} = {price}");
        else:
            await ctx.send("Não tem isso daí não.");
    except Exception as error:
            await ctx.send("Não ta funcionando, foi mal.");
            # BNBBTC

@bot.command(name = "segredo")
async def secret(ctx):
    try:
        await ctx.author.send("Segue nosso canal: twitch.tv/xenomorphzoid");
        await ctx.author.send("Me siga nas redes sociais: instagram.com/xenomorphzoid \ntwitter.com/xenomorphzoid");

    except discord.errors.Forbidden:
        await ctx.send("Não consigo te enviar nada em segredo, você tem algo contra mim?😭");

@tasks.loop(hours=1)
async def current_time():
    now = datetime.datetime.now();
    now = now.strftime("%d/%m/%Y às %H:%M");

    channel = bot.get_channel(0000000000000000);

    await channel.send("Data atual: " + now);

bot.run("000000kjsdfjs000000kask000");