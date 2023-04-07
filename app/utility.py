import threading
import yaml
from pathlib import Path

def build_config():
    try:
        my_path = Path(__file__).resolve()  # resolve to get rid of any symlinks
        config_path = my_path.parent / 'config.yaml'
        config = yaml.safe_load(open(config_path))
        return config
    except Exception as ex:
        print(f'Config file error: {ex}')

def debug_thread(fxn_name):
    print(f'{fxn_name}: {threading.get_ident()}')