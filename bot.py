import discord from discord.ext import commands
import os
import random from time import localtime, strftime

ct = strftime("%H:%M", localtime())
print(ct)

client = commands.Bot(command_prefix=".")
token = 'Nzc0MzYxODM0NzkwNTg0MzYw.X6WqqA.RAta8UBvx3YDM4qZjpQ30_mE49c'

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("I am online")

@client.command(name="scream")
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)


client.run(token)



