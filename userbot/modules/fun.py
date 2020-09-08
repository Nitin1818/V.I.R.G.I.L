from telethon.tl import types
from userbot.events import register
from userbot import bot

@register(outgoing=True, pattern="^.dart$")
async def dart(event):
  await event.edit("`Sending dart...`")
  await event.delete()
  await bot.send_file(event.chat.id, types.InputMediaDice('🎯'))


@register(outgoing=True, pattern="^.dice$")
async def dice(event):
  await event.edit("`Sending dice...`")
  await event.delete()
  await bot.send_file(event.chat.id, types.InputMediaDice('🎲'))
  
  
@register(outgoing=True, pattern="^.ball$")
async def ball(event):
  await event.edit("`Sending basketbaawait`")
  await event.delete()
  await bot.send_file(event.chat.id, types.InputMediaDice('🏀'))
  
  
@register(outgoing=True, pattern="^.fball$")
async def fball(event):
  await event.edit("`Sending football...`")
  await event.delete()
  await bot.send_file(event.chat.id, types.InputMediaDice('⚽'))
