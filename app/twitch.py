import requests
import socket
import json
from utility import *

    # TODO: token rotation for IRC oauth

def twitch_rfc(config, messages):
    debug_thread("twitch_rfc")
    try:
        if len(messages) > 0:
            sock = socket.socket()
            server = "irc.chat.twitch.tv"
            port = 6667
            nickname = f'{config["twitch_bot_user"]}' # twitch.tv bot viewer
            token = f'{config["twitch_bot_oauth"]}' # oauth token for twitch.tv bot
            channel = f'{config["twitch_channel"]}' # twitch channel where received TikTok messages are sent

            sock.connect((server, port))
            sock.send(f"PASS {token}\n".encode('utf-8' ))
            sock.send(f"NICK {nickname}\n".encode('utf-8'))
            sock.send(f"JOIN {channel}\n".encode('utf-8'))

            print('RFC connection made!')

            while True:
                for message in messages:
                    if not "twitch_chat" in message:
                        sock.send(f'PRIVMSG #{channel} :{message}\r\n'.encode('utf-8'))
                        print(f'twitch message--> {message}')

                sock.close()
                break
        else:
            print("No tiktok messages to process")
    except Exception as ex:
        print(ex)