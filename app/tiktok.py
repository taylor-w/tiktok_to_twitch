from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
from twitch import *

    # TODO: parameterize config (def build_config ?)

def tiktok_chat(res_list):
    print("tiktok_chat start")
    client: TikTokLiveClient = TikTokLiveClient(unique_id="@some_channel", **({
        "loop": "loop"
    }))

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