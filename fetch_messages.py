from telethon.sync import TelegramClient
import json
from telethon.tl.custom.message import Message

api_id = 24297707
api_hash = '8837dd93f8baeafcc57e9e472a695dcc'

client = TelegramClient('softvintech_session', api_id, api_hash)

async def fetch_messages():
    channel_url = 'https://t.me/+Gu5q7uvRWDY3ZThk'
    await client.start()
    channel = await client.get_entity(channel_url)

    result = []
    async for message in client.iter_messages(channel, limit=500):
        if isinstance(message, Message) and message.message:
            result.append({"text": message.message, "date": str(message.date)})

    with open("messages.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

with client:
    client.loop.run_until_complete(fetch_messages())

