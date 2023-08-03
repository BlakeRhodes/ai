import argparse

from ai.config import get_config

parser = argparse.ArgumentParser(description='Power your shell with AI')
parser.add_argument('--key', default=get_config()['openaiKey'], help='Your OpenAI API key')
parser.add_argument('--temperature', default=0, type=float,
                    help='Tempature of the AI for generating commands (default: 0)')
parser.add_argument('--shell', default='bash', help='The shell to generate the commands for (default: bash)')
parser.add_argument('--verbose', default=False, action='store_true',
                    help='Turn on logging for agent\'s reasoning (default: False)')

parser.add_argument('prompt', nargs='+', help='This is the prompt the AI will use to generate the command')
arguments = parser.parse_args()


