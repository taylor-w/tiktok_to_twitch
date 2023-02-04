# tiktok_to_twitch
An integration that sends tiktok messages from a defined tiktok channel to a defined twitch chat, under "some_user" account (`tiktok_chatter` by default)

## How-to Deploy Service
Currently just a script, so the referenced python `import`s will need installed as well as python to execute the code:
1. `pip isntall <all_imports>`
2. `cd tiktok-chat/app`
3. `python main.py`

## Future-state
Make this script serviceable so end-user can execute more directly

## TODOs
- `build_config()` or similar for passing config values
- proper config values
- key rotation for RFC connection (`twitch.py` file)

## References
tba