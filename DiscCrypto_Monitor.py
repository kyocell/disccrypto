#                   Made by Kyocell
#
# Contact - Kyocell#1491 (Discord) for help setting up
#
#
# Please do credit if you use this bot :D (Github)
#
#



#
# Make sure to go through/edit this file carefully to change stuff to your choice.
#




import discord
from discord.ext import commands
from discord.ext import tasks
import random
from pytwitterscraper import TwitterScraper
from pycoingecko import CoinGeckoAPI
from itertools import cycle
from datetime import datetime
import asyncio


statuses = cycle(['Monitoring Crypto\n\ndiscord.gg/JBwnGN7GMv', '$help\n\ndiscord.gg/JBwnGN7GMv'])
client = commands.Bot(command_prefix="$")

now = datetime.now()


@client.event
async def on_ready():
    change_status.start()
    _btc1d.start()
    _doge1d.start()
    _btc1h.start()
    _doge1h.start()
    _btc5m.start()
    _doge5m.start()
    print(f"{client.user} is ready!")


@tasks.loop(seconds=10.0)
async def change_status():
    await client.change_presence(activity=discord.Game(next(statuses)))


@client.event
async def on_member_join(member):
    print(f"{member} has arrived.")
    welcome = client.get_channel(808360129837400095)
    await welcome.send(f"{member} has arrived.")


async def on_member_remove(member):
    print(f"pce {member}")
    bye = client.get_channel(808360129837400095)
    await bye.send(f"pce {member}")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! ({round(client.latency * 1000)})")


@client.command(aliases=["8ball"])
async def _8ball(ctx):
    responses = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    await ctx.send(f"{random.choice(responses)}")


@client.command(aliases=["del", 'clear'])
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=["gettweet", "gtweet"])
async def get_twt(ctx, *, ID):
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    tw = TwitterScraper()
    twt = tw.get_tweets(ID)
    await ctx.send(f"{twt.contents[0]['text']}")



cg = CoinGeckoAPI()

@client.command(aliases=['coinprice'])
async def coin_info(ctx, id, currency):
    try:
        response = cg.get_price(ids=id.lower(), vs_currencies=currency.lower())
        coin_embed = discord.Embed(title=f"Coin : {id.upper()}", description=f"{id.upper()} vs {currency.upper()}")
        coin_embed.add_field(name=id.upper(), value=response[f'{id.lower()}'][f'{currency.lower()}'], inline=False)
        await ctx.send(embed=coin_embed)
    except:
        ctx.send("The correct usage is - $coinprice <coinname> <currency>! (lowercases)")


                   
                   
# Make sure to edit the discord channel ids before you run the script!                   
                   
                   


@tasks.loop(seconds=86400.0)
async def _btc1d():
    price_change = cg.get_price(ids='bitcoin', vs_currencies='usd')
    await asyncio.sleep(86100)
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    if price_change['bitcoin']['usd'] > price['bitcoin']['usd']:
        btc1d = client.get_channel(808357840023715871)
        btc1d_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc1d_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0x1f8b4c)
        btc1d_embed.add_field(name="Price", value=f"{btc1d_updater['bitcoin']['usd']}", inline=True)
        btc1d_embed.add_field(name="Currency", value="USD", inline=True)
        btc1d_embed.set_author(name="Crypto Monitor",
                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        btc1d_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await btc1d.send(embed=btc1d_embed)
    else:
        btc1d = client.get_channel(808357840023715871)
        btc1d_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc1d_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0xe74c3c)
        btc1d_embed.add_field(name="Price", value=f"{btc1d_updater['bitcoin']['usd']}", inline=True)
        btc1d_embed.add_field(name="Currency", value="USD", inline=True)
        btc1d_embed.set_author(name="Crypto Monitor",
                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        btc1d_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await btc1d.send(embed=btc1d_embed)


@tasks.loop(seconds=86400)
async def _doge1d():
    price_change = cg.get_price(ids='dogecoin', vs_currencies='inr')
    await asyncio.sleep(86100)
    price = cg.get_price(ids='dogecoin', vs_currencies='inr')
    if price_change['dogecoin']['inr'] > price['dogecoin']['inr']:
        doge1d = client.get_channel(808357910555525120)
        doge1d_updater = cg.get_price(ids='dogecoin', vs_currencies='inr')
        doge1d_embed = discord.Embed(title=f"Doge", description=f"Doge vs INR", colour=0x1f8b4c)
        doge1d_embed.add_field(name="Price", value=f"{doge1d_updater['dogecoin']['inr']}", inline=True)
        doge1d_embed.add_field(name="Currency", value="INR", inline=True)
        doge1d_embed.set_author(name='Crypto Monitor', icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
        doge1d_embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await doge1d.send(embed=doge1d_embed)
    else:
        doge1d = client.get_channel(808357910555525120)
        doge1d_updater = cg.get_price(ids='dogecoin', vs_currencies='inr')
        doge1d_embed = discord.Embed(title=f"Doge", description=f"Doge vs INR", colour=0xe74c3c)
        doge1d_embed.add_field(name="Price", value=f"{doge1d_updater['dogecoin']['inr']}", inline=True)
        doge1d_embed.add_field(name="Currency", value="INR", inline=True)
        doge1d_embed.set_author(name='Crypto Monitor',
                                icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
        doge1d_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await doge1d.send(embed=doge1d_embed)



@tasks.loop(seconds=3600.0)
async def _btc1h():
    price_change = cg.get_price(ids='bitcoin', vs_currencies='usd')
    await asyncio.sleep(3300)
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    if price_change['bitcoin']['usd'] > price['bitcoin']['usd']:
        btc1h = client.get_channel(808357866062348318)
        btc1h_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc1h_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0x1f8b4c)
        btc1h_embed.add_field(name="Price", value=f"{btc1h_updater['bitcoin']['usd']}", inline=True)
        btc1h_embed.add_field(name="Currency", value="USD", inline=True)
        btc1h_embed.set_author(name="Crypto Monitor",
                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        btc1h_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await btc1h.send(embed=btc1h_embed)
    else:
        btc1h = client.get_channel(808357866062348318)
        btc1h_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc1h_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0xe74c3c)
        btc1h_embed.add_field(name="Price", value=f"{btc1h_updater['bitcoin']['usd']}", inline=True)
        btc1h_embed.add_field(name="Currency", value="USD", inline=True)
        btc1h_embed.set_author(name="Crypto Monitor",
                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        btc1h_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await btc1h.send(embed=btc1h_embed)



@tasks.loop(seconds=3600.0)
async def _doge1h():
    price_change = cg.get_price(ids='dogecoin', vs_currencies='inr')
    await asyncio.sleep(3300)
    price = cg.get_price(ids='dogecoin', vs_currencies='inr')
    if price_change['dogecoin']['inr'] > price['dogecoin']['inr']:
        doge1h = client.get_channel(808357927441137674)
        doge1h_updater = cg.get_price(ids='dogecoin', vs_currencies='inr')
        doge1h_embed = discord.Embed(title=f"Doge", description=f"Doge vs INR", colour=0x1f8b4c)
        doge1h_embed.add_field(name="Price", value=f"{doge1h_updater['dogecoin']['inr']}", inline=True)
        doge1h_embed.add_field(name="Currency", value="INR", inline=True)
        doge1h_embed.set_author(name='Crypto Monitor', icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
        doge1h_embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await doge1h.send(embed=doge1h_embed)
    else:
        doge1h = client.get_channel(808357927441137674)
        doge1h_updater = cg.get_price(ids='dogecoin', vs_currencies='inr')
        doge1h_embed = discord.Embed(title=f"Doge", description=f"Doge vs INR", colour=0xe74c3c)
        doge1h_embed.add_field(name="Price", value=f"{doge1h_updater['dogecoin']['inr']}", inline=True)
        doge1h_embed.add_field(name="Currency", value="INR", inline=True)
        doge1h_embed.set_author(name='Crypto Monitor',
                                icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
        doge1h_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await doge1h.send(embed=doge1h_embed)



@tasks.loop(seconds=300.0)
async def _btc5m():
    price_change = cg.get_price(ids='bitcoin', vs_currencies='usd')
    await asyncio.sleep(270)
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    if price_change['bitcoin']['usd'] > price['bitcoin']['usd']:
        btc5m = client.get_channel(808357886953652224)
        btc5m_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc5m_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0x1f8b4c)
        btc5m_embed.add_field(name="Price", value=f"{btc5m_updater['bitcoin']['usd']}", inline=True)
        btc5m_embed.add_field(name="Currency", value="USD", inline=True)
        btc5m_embed.set_author(name="Crypto Monitor",
                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        btc5m_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await btc5m.send(embed=btc5m_embed)
    else:
        btc5m = client.get_channel(808357886953652224)
        btc5m_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
        btc5m_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0xe74c3c)
        btc5m_embed.add_field(name="Price", value=f"{btc5m_updater['bitcoin']['usd']}", inline=True)
        btc5m_embed.add_field(name="Currency", value="USD", inline=True)
        btc5m_embed.set_author(name="Crypto Monitor",
                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
        btc5m_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await btc5m.send(embed=btc5m_embed)




@tasks.loop(seconds=300.0)
async def _doge5m():
    price_change = cg.get_price(ids='dogecoin', vs_currencies='inr')
    await asyncio.sleep(270)
    price = cg.get_price(ids='dogecoin', vs_currencies='inr')
    if price_change['dogecoin']['inr'] > price['dogecoin']['inr']:
        doge5m = client.get_channel(808367220794982420)
        doge5m_updater = cg.get_price(ids='dogecoin', vs_currencies='inr')
        doge5m_embed = discord.Embed(title=f"Doge", description=f"Doge vs INR", colour=0x1f8b4c)
        doge5m_embed.add_field(name="Price", value=f"{doge5m_updater['dogecoin']['inr']}", inline=True)
        doge5m_embed.add_field(name="Currency", value="INR", inline=True)
        doge5m_embed.set_author(name='Crypto Monitor', icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
        doge5m_embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await doge5m.send(embed=doge5m_embed)
    else:
        doge5m = client.get_channel(808367220794982420)
        doge5m_updater = cg.get_price(ids='dogecoin', vs_currencies='inr')
        doge5m_embed = discord.Embed(title=f"Doge", description=f"Doge vs INR", colour=0xe74c3c)
        doge5m_embed.add_field(name="Price", value=f"{doge5m_updater['dogecoin']['inr']}", inline=True)
        doge5m_embed.add_field(name="Currency", value="INR", inline=True)
        doge5m_embed.set_author(name='Crypto Monitor',
                                icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
        doge5m_embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
        await doge5m.send(embed=doge5m_embed)


                               
                               
                               
# This is just a test example of an embed reply from the bot -

#@client.command(aliases=['embed'])
#async def embed_test(ctx):
#    embedVar = discord.Embed(title="BTC", description="Bitcoin vs Inr", color=0x00ff00)
#    embedVar.add_field(name="Price", value="50000", inline=True)
#    embedVar.add_field(name="Currency", value="USD", inline=True)
#    embedVar.set_author(name="Crypto Monitor", icon_url="https://camo.githubusercontent.com/94b5f3bae21ae60db73a4092fb17a1432796651a991751c19a4683328e014af2/687474703a2f2f7374617469632e74756d626c722e636f6d2f7070646a3579392f4165396d786d7874702f333030636f696e2e706e67")
#    embedVar.set_thumbnail(url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
#    await ctx.send(embed=embedVar)


                               
                               
                               
# This is an example of the profit/loss coloured response from the bot
# Basically, if the value of a particular crypto rises, it sends the embeded message in green color indicating rise and vice-e-versa.
#Remove the '#' from the below loop block to activate it.

#@tasks.loop(seconds=15)
#async def prof_loss_price():
#    price_change = cg.get_price(ids='bitcoin', vs_currencies='usd')
#    await asyncio.sleep(10)
#    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
#    if price_change['bitcoin']['usd'] > price['bitcoin']['usd']:
#        btc5m = client.get_channel(726377826152087625)
#        btc5m_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
#        btc5m_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0x1f8b4c)
#        btc5m_embed.add_field(name="Price", value=f"{btc5m_updater['bitcoin']['usd']}", inline=True)
#        btc5m_embed.add_field(name="Currency", value="USD", inline=True)
#        btc5m_embed.set_author(name="Crypto Monitor",
#                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
#        btc5m_embed.set_thumbnail(
#            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
#        await btc5m.send(embed=btc5m_embed)
#    else:
#        btc5m = client.get_channel(726377826152087625)
#        btc5m_updater = cg.get_price(ids='bitcoin', vs_currencies='usd')
#        btc5m_embed = discord.Embed(title=f"BTC", description=f"Bitcoin vs USD", colour=0xe74c3c)
#        btc5m_embed.add_field(name="Price", value=f"{btc5m_updater['bitcoin']['usd']}", inline=True)
#        btc5m_embed.add_field(name="Currency", value="USD", inline=True)
#        btc5m_embed.set_author(name="Crypto Monitor",
#                               icon_url="https://st3.depositphotos.com/5906102/14454/v/600/depositphotos_144548047-stock-illustration-crypto-currency-bitcoin-golden-symbol.jpg")
#        btc5m_embed.set_thumbnail(
#            url="https://cdn.discordapp.com/avatars/802976971276550166/896230be1048bb539ffc0d36b4cc3639.png?size=128")
#        await btc5m.send(embed=btc5m_embed)




client.run('Your Bot Token here')
