import json
from pathlib import Path


def get_config():
    with open(f'{Path.home()}/.ai-config') as f:
        data = f.read()
    f.close()
    config: dict = json.loads(data)

    if not config.get('openaiKey'):
        raise Exception('OpenAI API key not found. Please set it in ~/.ai-config')
    if not config.get('shell'):
        config['shell'] = 'bash'
    return config
