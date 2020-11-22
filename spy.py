#coding=UTF-8
import discord
import requests
import asyncio

client = discord.Client()

spyChannels = [1234, 4321, 1337]
webhookUrl = "https://discord.com/api/webhooks/FAKE/WEBHOOK"

@client.event
async def on_ready():
  print('spy running as ' + client.user.name + "#" + client.user.discriminator)

@client.event
async def on_message(message):
  if message.channel.id in spyChannels:
    if message.attachments:
      attachment = message.attachments[0]
      requests.post(webhookUrl, data={'content': message.content + "\n*Attachment: " + attachment.url + "*", 'username': message.author.name + ' [#' + message.channel.name + ']', 'avatar_url' : str(message.author.avatar_url)})
    else:
      requests.post(webhookUrl, data={'content': message.content, 'username': message.author.name + ' [#' + message.channel.name + ']', 'avatar_url' : str(message.author.avatar_url)})

print('Starting...')
client.run("TOKEN", bot=False)
