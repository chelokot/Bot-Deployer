import asyncio
import telethon
from telethon import TelegramClient, events
import os
import sys

import time
last_check = time.time() - 1000

api_id = 18661652
api_hash = 'f45d0b5647ddc06191a23d881a595952'

import json
with open('prepods/correspondence.json', 'r') as f:
    correspondence = json.load(f)["map"]

async def main():
    global last_check
    try:
        client.disconnect()
    except:
        pass
    try:  
        try:
            client = TelegramClient('session_name', api_id, api_hash)
            await client.start()
        except Exception as e:
            os.chdir(sys.path[0])
            if f"{'session_name'}.session" in os.listdir():
                os.remove(f"{'session_name'}.session")
            client = TelegramClient('session_name', api_id, api_hash)
            await client.start()


        @client.on(events.Raw)
        async def handler0(event):
            """
            This is just trick to send message to bot every second
            """
            global last_check
            if time.time() - last_check > 600 and time.localtime().tm_hour >= 7 and time.localtime().tm_hour <= 15:
                last_check = time.time()
                await client.send_message("@nikita_kolos_bot", "пара")

        @client.on(events.NewMessage)
        async def process_answer(event: events.NewMessage.Event):
            """
            This function checks if we got answer from bot, and if so, prints it
            """
            if event.chat_id == 1208868324:
                text = event.message.message
                text = text.split('Следующая пара')[0]

                prepod = None
                for item in correspondence:
                    if item["subject"] in text:
                        prepod = item["prepod"]
                        break
                
                if prepod is not None:
                    await client.send_message('@BotFather', '/setname')
                    time.sleep(1)
                    await client.send_message('@BotFather', "@nikita_kolos_bot")
                    time.sleep(1)
                    await client.send_message('@BotFather', prepod["name"])
                    time.sleep(1)
                    await client.send_message('@BotFather', '/setabouttext')
                    time.sleep(1)
                    await client.send_message('@BotFather', "@nikita_kolos_bot")
                    time.sleep(1)
                    await client.send_message('@BotFather', prepod["bio"])
                    time.sleep(1)
                    await client.send_message('@BotFather', '/setabouttext')
                    time.sleep(1)
                    await client.send_message('@BotFather', "@nikita_kolos_bot")
                    time.sleep(1)
                    await client.send_message('@BotFather', prepod["bio"])
                    time.sleep(1)
                    await client.send_message('@BotFather', '/setdescription')
                    time.sleep(1)
                    await client.send_message('@BotFather', "@nikita_kolos_bot")
                    time.sleep(1)
                    await client.send_message('@BotFather', prepod["bio"])
                    time.sleep(1)
                    await client.send_message('@BotFather', '/setuserpic')
                    time.sleep(1)
                    await client.send_message('@BotFather', "@nikita_kolos_bot")
                    time.sleep(1)
                    await client.send_file('@BotFather', os.path.join("prepods", prepod["pp"]))


        await client.run_until_disconnected()


    except Exception as e:
        print(e)
        await client.disconnect()

asyncio.run(main())
