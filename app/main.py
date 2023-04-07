import asyncio
import sys
import threading
from tiktok import *
from utility import *
from build_config import *
from time import sleep

# TODO: Add 'debug' mode in config where 'debug' substitutes bot's channel and a random tiktok live, for testing

def main():
    debug_thread("main")
    config = build_config()

    sys.tracebacklimit = 0
    res_list = []
    sleep_counter = 0
    backoff_seconds = 60

    while True:
        while True:
            try:
                # 1 thread to async run tiktok_chat on res_list
                print("t1 init")
                t1 = threading.Thread(target=tiktok_chat, args=(config, res_list), daemon=True)
                print("t1 start")
                t1.start()
                print("t1 join")
                t1.join()
            except Exception as ex:
                print(f'Error in coroutine, ending main: {ex}')
            print("is t1 alive?")
            if t1.is_alive():
                continue
            else:
                # 1. 60 secs, 2. 120 sec, 3. 440 secs, 4. 880 secs, 5. 1760 secs, 6. 3600 secs
                if sleep_counter == 0:
                    backoff_seconds = 60
                elif sleep_counter == 1:
                    backoff_seconds = backoff_seconds * 2
                elif sleep_counter == 2:
                    backoff_seconds = backoff_seconds * 3
                elif sleep_counter == 3:
                    backoff_seconds = backoff_seconds * 4
                else:
                    backoff_seconds = 3600
                print(f'Tiktok user offline, sleeping thread: {backoff_seconds}...')
                sleep(backoff_seconds)
                sleep_counter += 1
                break

if __name__ == '__main__':
    debug_thread("__main__")

    # call main
    main()
