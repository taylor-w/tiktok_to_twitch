from TikTokLive import *# TikTokLiveClient
from TikTokLive.types.events import * #CommentEvent, ConnectEvent, DisconnectEvent, LiveEndEvent, WeeklyRankingEvent
from twitch import *
from utility import *
from time import sleep
import asyncio

def tiktok_chat(config, res_list):
    debug_thread("tiktok_chat")
    try:
        print("tiktok_chat start")
        client: TikTokLiveClient = TikTokLiveClient(unique_id=f'@{config["tiktok_channel"]}', **({
            "loop": "loop"
        }))

        @client.on("live_end")
        async def on_connect(event: LiveEndEvent):
            print(f"Livestream ended :(")
            await asyncio.sleep(3.14)
            client.stop()

        @client.on("disconnect")
        async def on_disconnect(event: DisconnectEvent):
            print("Disconnected")
            await asyncio.sleep(3.14)
            client.stop()

        # Notice no decorator?
        @client.on("comment")
        async def on_comment(event: CommentEvent):
            # add tiktok msg to list
            res_list.append(f"{event.user.nickname}: {event.comment}")
            # send tiktok msg list to twitch_rfc to process
            twitch_rfc(config, res_list)
            # remove tiktok msg from list so it's sent again
            res_list.remove(f"{event.user.nickname}: {event.comment}")

        # Run the client and block the main thread
        # await client.start() to run non-blocking
        asyncio.run(client.start())
    except Exception as ex:
        print(ex)
