import threading

def debug_thread(fxn_name):
    print(f'{fxn_name}: {threading.get_ident()}')