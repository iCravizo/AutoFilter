API_ID = 11726518
API_HASH = "62fc537f4c4894086b160f9c2cdfe21c"
SESSION_NAME = "AQEbHpUAE3NFI1e3knhiHhuGydFX-4nmr401Opc3yh200FBUcVpPQWHzGZoO6XuT8_v9gXMDgGdvEFGaOfDDAWyA9Cg3xcdp_N3lG2taDeQzF2i-K-UHF5pmt-311kXqcyjK0cbN-YblccrlEMOwt7fAxPcJBdyhoWBUQ6OBUvrrxHlyJxdj3PgUpMS8lSmkiYeSPU339oiXDd6CNwS6Lq-17QCnOzcZueErkfqDpMiql2SMeMQewp-DHeIrhVk7PA-yDebGh5r54BVxfarvbvnhex66xffHVyjXpspNLd2EatOazlq6lmbjZtFRiY44Ni5NC7HdKYJfod6ZS0Zz7JjxQ2xvUQAAAABnIt8iAA"
BOT_TOKEN = "5760159870:AAEKlrDpiaMtOsjoCbgIEEUuMdXNyK07Z5A"
CHANNEL_ID = -1001617140233
CHANNEL_LINK = 'https://t.me/AskMovie8'
AUTH_GROUP = '@AskMovie3'
BANNED_WORDS = [
    'shareus',
    'in',
    'link',
    'links',
    'dubbed',
    'full',
    'movie',
    'url',
    'openurl',
    'how',
    'to',
    'open',
    1,
    '1',
    2,
    '2',
    3,
    '3',
    4,
    '4',
    5,
    '5',
    6,
    '6',
    7,
    '7',
    8,
    '8',
    9,
    '9',
    0,
    '0',
]

from pyropatch import flood_handler

flood_handler
from asyncio import sleep as slp
from pyrogram import Client, filters, idle
from pyromod.helpers import ikb
from pyrogram.types import Message

Bot = Client("Bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

User = Client("user",
              api_id=API_ID,
              api_hash=API_HASH,
              session_string=SESSION_NAME)


@Bot.on_message(filters.private & filters.command("start"))
async def start_handler(_, event: Message):
    await event.reply_text(
        f"Hi! {event.from_user.mention} \n\nThis is a bot for @askmovie3 and @askmovie8\n\n\nBote Made By @s4tyendra\nContact if you want any type of bots."
    )


@Bot.on_message(filters.chat([AUTH_GROUP, 'S4tyendra']))
async def text(_, event):
    tyt = str((event.text).lower())
    if tyt in BANNED_WORDS:
        mfd = await event.reply('😒ok😒', quote=True)
        await slp(5)
        await mfd.delete()
    elif len(tyt.split(" ")) > 4:
        print('.')
    else:
        answers = []
        async for message in User.search_messages(chat_id=CHANNEL_ID,
                                                  limit=10000,
                                                  query=event.text):
            answers.append(f"{CHANNEL_LINK}/{message.id}")

        nswers = [answers[i:i + 30] for i in range(0, len(answers), 30)]
        for i in nswers:
            lt = []
            for n in list(i):
                mid = n.split('/')[4]
                gd = await Bot.get_messages(CHANNEL_ID, int(mid))
                fgh = str(gd.caption)
                tta = str(fgh.split('\n', 1)[0]).replace('Title: ', '')
                lt.append([(f'{tta}', f'{n}', 'url')])
            msg = '\n'.join([str(mm) + '\n' for mm in list(i)])
            mg = await event.reply(
                f'**HERE ARE THE RESULTS FOR YOUR SEARCH**\n\n{msg}',
                quote=True,
                disable_web_page_preview=True,
                reply_markup=ikb(lt))
            #await slp(300)
            #await mg.delete()


Bot.start()
User.start()
print(f'{Bot.get_me().username} Started!')
idle()
Bot.stop()
User.stop()
