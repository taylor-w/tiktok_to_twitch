import asyncio
import threading
from tiktok import *

def main():
    res_list = []
    # 1 thread to async run tiktok_chat on res_list
    t1 = threading.Thread(target=asyncio.run, args=(tiktok_chat(res_list), ))
    t1.start()
    t1.join()

if __name__ == '__main__':
    # asyncio set event loop policy for windows compliance
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # call main
    main()
