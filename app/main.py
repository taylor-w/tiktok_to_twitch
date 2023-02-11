import asyncio
import sys
import threading
from tiktok import *

# TODO: Add 'debug' mode in config where 'debug' substitutes bot's channel and a random tiktok live, for testing

def main():
    sys.tracebacklimit = 0
    res_list = []
    # 1 thread to async run tiktok_chat on res_list
    t1 = threading.Thread(target=asyncio.run, args=(tiktok_chat(res_list), ))

    while True:
        try:
            t1.start()
            t1.join()
        except asyncio.CancelledError:
            print("Error in coroutine, ending main")
        if t1.is_alive():
            continue
        else:
            break

if __name__ == '__main__':
    # asyncio set event loop policy for windows compliance
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # call main
    main()
