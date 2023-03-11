import yaml

def build_config():
    try:
        config = yaml.safe_load(open("config.yaml"))
        return config
    except Exception as ex:
        print(f'Config file error: {ex}')