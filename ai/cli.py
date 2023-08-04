import argparse

from ai.config import get_config

config = get_config()

parser = argparse.ArgumentParser(description='Power your shell with AI')
parser.add_argument('--key', default=config['openaiKey'], help='Your OpenAI API key')
parser.add_argument('--temperature', default=0, type=float,
                    help='Temperature of the AI for generating commands (default: 0)')
parser.add_argument('--shell', default=config['shell'], help='The shell to generate the commands for (default: bash)')
parser.add_argument('--verbose', default=False, action='store_true',
                    help='Turn on logging for agent\'s reasoning (default: False)')

parser.add_argument('prompt', nargs='+', help='This is the prompt the AI will use to generate the command')


def get_arguments():
    return parser.parse_args()
