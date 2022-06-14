from os import system
from pyngrok import conf,ngrok
import re
import asyncio
import socket
import os
import discord
import random
import subprocess

#Discord config
discord_token = "discord token"
discord_channel = channel id

#Tunnel configuration
ngrok_token = "ngrok token"
port = 12345

#NOIP Credentials
email = "your noip email"
password = "your noip pass"
hostname = "name of your noip hostname(for example - pastel.ddns.net)"

hi = [
    'hi',
	'hey',
    'hello',
    'Hello!',
    'Hey, how are You?',
    'Good to see you!',
    'Welcome',
]

client = discord.Client()

ngrok.set_auth_token(ngrok_token)
conf.get_default().region = "eu"

ngrok.connect(port, "tcp")

tunnels = ngrok.get_tunnels()
tunnellist = re.findall('"([^"]*)"', str(tunnels))

ngrokurl = str(tunnellist[0])
ngrokurl = ngrokurl.removeprefix('tcp://')

ngrokport = str(ngrokurl.split(":", 1)[1])

ngrokurl = str(ngrokurl.split(":", 1)[0])

ngrokip = socket.gethostbyname(ngrokurl)

os.system(f"noipy -u {email} -p {password} -n {hostname} --provider noip {ngrokip}")
print(" ")
print(f"The server runs on direct {ngrokurl}, IP {ngrokip}, hostname {hostname}, and port {ngrokport}.")

@client.event
async def on_ready():
    await client.wait_until_ready()
    channel = client.get_channel(discord_channel)
    await channel.send(f"Server is accessible on: `{hostname}:{ngrokport}` or `{ngrokip}:{ngrokport}`")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('^ping'):
        msg = await message.channel.send("Pinging...")
        pingddns = subprocess.getoutput(f"ping -s 53 -c 1 {hostname}")
        a = re.search('time=(.+?)ms', pingddns)
        if a:
            pingresponseddns = a.group(1)

        pingngrok = subprocess.getoutput(f"ping -s 53 -c 1 {ngrokip}")
        b = re.search('time=(.+?)ms', pingngrok)
        if b:
            pingresponsengrok = b.group(1)
        await asyncio.sleep(1)
        await msg.edit(content=f"The server's ping is:\nDDNS: `{pingresponseddns}ms`\nDirect: `{pingresponsengrok}ms`")

    if message.content in hi:
        response = random.choice(hi)
        await message.channel.send(response)


client.run(discord_token)