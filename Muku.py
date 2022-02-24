import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply(
    "__**𝐈'𝐦 ⚡️ 𝐀𝐋𝐈𝐄𝐍 𝐓𝐀𝐆 ⚡️**, 𝐢 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐀𝐥𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐈𝐧 𝐆𝐫𝐨𝐮𝐩 𝐎𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🥀\n𝐂𝐥𝐢𝐜𝐤 **/help** 𝐅𝐨𝐫 𝐌𝐨𝐫𝐞 𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧__\n\n 𝐅𝐨𝐥𝐥𝐨𝐰 [𝐀𝐋𝐈𝚵𝐍™ 𝐗](https://t.me/ALIEN_X_SUPPORT) 𝗢𝗻 𝐓𝐞𝐥𝐞𝐆𝐫𝐚𝐦",
    link_preview=False,
    buttons=(
      [
        Button.url('🛠 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 ⚒', 'https://t.me/ALIEN_X_SUPPORT'),
        Button.url('𝐑𝚵𝐏𝐎 💥', 'https://github.com/Legend-Mukund/TAG-BOT'),
        Button.url('🦋 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 🦋', 'https://telegra.ph/ALIEN-MENTION-ROBOT-COMMANDS-01-25-2')  
      ]
    )
  )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Help Menu of 𝐀𝐋𝐈𝐄𝐍 𝐓𝐀𝐆 Bot**\n\nCommand: /all\n__You can use this command with text what you want to mention others.__\nExample: `/all HOI GUYS KEMCHO !`\n__You can you this command as a reply to any message. Bot will tag users to that replied messsage__.\n\nUse /cancel To Stop Tagging in group\n\nFollow [𝐀𝐋𝐈𝚵𝐍™ 𝐗](https://t.me/ALIEN_X_SUPPORT) 𝗢𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('🛠 𝙎𝙐𝙋𝙋𝙊𝙍𝙏 ⚒', 'https://t.me/ALIEN_X_SUPPORT'),
        Button.url('⚡️𝐀𝐃𝐃 𝐌𝚵 ⚡️', 'https://t.me/ALIEN_MENTION_ROBOT?startgroup=true'),
        Button.url('🦋 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 🦋', 'https://telegra.ph/ALIEN-MENTION-ROBOT-COMMANDS-01-25-2')
      ]
    )
  )
    
@client.on(events.NewMessage(pattern="^/repo$"))
async def help(event):
  helptext = "**ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʀᴇᴘᴏ ᴏꜰ ᴛʜᴇ ᴀʟɪᴇɴ x ᴛᴀɢ ʀᴏʙᴏᴛ ᴊᴏɪɴ  [*•.¸♡ ❥𝐀𝐋𝐈𝚵𝐍™ 𝐗ఌ ♡¸.•*](https://t.me/ALIEN_X_SUPPORT) ɪꜰ ᴜ ʜᴀᴠᴇ ᴀɴʏ Qᴜᴇʀʏ.**"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('𝐑𝚵𝐏𝐎 💥', 'https://github.com/Legend-Mukund/TAG-BOT'),
        Button.url('𝐒𝐔𝐏𝐏𝐎𝐑𝐓 👻', 'https://t.me/ALIEN_X_SUPPORT')
      ]
    )
  )    
  
@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def all(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__This command Can Be Use In Groups And Channels !!!__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__Only Admins Can Mention All\n\nFor More Go On @ALIEN_X_SUPPORT !!!__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__Give me one argument!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__I Can't Mention Members For Older Messages! (messages which are sent before I'm added to group)__")
  else:
    return await event.respond("__Reply To a Message Or Give Me Some Text To Mention Others !!!__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}\n\nMade by [𝐌𝐔𝐊𝐔𝐍𝐃](https://t.me/ABOUT_MUKUND) 💥❤️"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__There Is No Proccess On Going...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__Stopped.__')

print(">> MUKU TAGALL BOT STARTED @ALIEN_X_SUPPORT ❤️<<")
client.run_until_disconnected()
