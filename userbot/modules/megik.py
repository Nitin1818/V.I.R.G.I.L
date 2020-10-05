from userbot.events import register
from userbot import bot
from telethon.tl.functions.messages import UpdatePinnedMessageRequest

# module by Nitin1818
@register(outgoing=True, pattern="^.megik$")
async def bmegik(event):
  if not event.is_group:
    await event.edit("**I don't think this is a group**")
    return
  
  chat = await event.get_chat()
  admin = chat.admin_rights
  creator = chat.creator
  
  if not admin and not creator:
    await event.edit("`Im not admeme sed -_-`")
    return
  
  try:
    await bot(UpdatePinnedMessageRequest(event.to_id, event.reply_to_msg_id == None))
  except BadRequestError:
        await event.edit("I don't have sufficient permissions to update this chat")
        return
  await event.edit(f"`Here we go` **{event.chat.title}** `updated Successfully!`")
