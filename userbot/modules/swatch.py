from userbot.events import register
from userbot import bot, spamwtc
from time import sleep

swbans = spamwtc.stats()

@register(outgoing=True, pattern="^.sw$")
async def swatch(event):
  if not event.is_group:
    await event.edit("**I don't think this is a group**")
    return
  
  i = 0
  chat = await event.get_chat()
  admin = chat.admin_rights
  creator = chat.creator
  
  if not admin and not creator:
    await event.edit("`I'm not admeme sed -_-`")
    return
  await event.edit(f"`I'm gonna remove spamwatch banned users from` **{event.chat.title}!**")
  i = 0
        
  async for x in event.client.iter_participants(event.chat_id):
    if spamwtc.get_ban(x.id):
        await bot.kick_participant(event.chat_id, x.id)
        sleep(2)
        i += 1
  await event.edit(f"**Result: No. of** `{i}` `User has been removed couz they was banned in spamwatch`\n **Count:** `{swbans}`")
