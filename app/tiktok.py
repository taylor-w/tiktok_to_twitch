from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, DisconnectEvent, LiveEndEvent, WeeklyRankingEvent
from twitch import *
from time import sleep
import sys

    # TODO: parameterize config (def build_config ?)

def tiktok_chat(res_list):
    try:
        print("tiktok_chat start")
        client: TikTokLiveClient = TikTokLiveClient(unique_id="@<some_tiktok_channel>", **({
            "loop": "loop"
        }))

        @client.on("live_end")
        async def on_connect(event: LiveEndEvent):
            print(f"Livestream ended :(")
            sys.exit()

        @client.on("disconnect")
        async def on_disconnect(event: DisconnectEvent):
            print("Disconnected")
            sleep(30) # sleep 30 seconds if disconnected
            await client.reconnect()

        # Notice no decorator?
        @client.on("comment")
        async def on_comment(event: CommentEvent):
            # add tiktok msg to list
            res_list.append(f"{event.user.nickname}: {event.comment}")
            # send tiktok msg list to twitch_rfc to process
            twitch_rfc(res_list)
            # remove tiktok msg from list so it's sent again
            res_list.remove(f"{event.user.nickname}: {event.comment}")

        # Run the client and block the main thread
        # await client.start() to run non-blocking
        client.run()
    except Exception as ex:
        print(ex)
