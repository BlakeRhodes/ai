import json
from pathlib import Path


def get_config():
    with open(f'{Path.home()}/.ai-config') as f:
        data = f.read()
    f.close()
    return json.loads(data)