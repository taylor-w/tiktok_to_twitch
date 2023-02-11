import requests
import socket
import json

    # TODO: parameterize config (def build_config ?)
    # TODO: token rotation for IRC oauth

def twitch_rfc(messages):
    if messages:
        sock = socket.socket()
        server = "irc.chat.twitch.tv"
        port = 6667
        nickname = "tiktok_chatter" # twitch.tv bot viewer
        token = "" # oauth token for twitch.tv bot
        channel = "tiktok_chatter" # twitch channel where received TikTok messages are sent

        sock.connect((server, port))
        sock.send(f"PASS {token}\n".encode('utf-8'))
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