# AI Shell Assistant 🤖💻

AI Shell Assistant is a Python-based, AI-powered application that generates shell scripts based on natural language prompts. It's like having your own personal AI assistant that's powered by OpenAI!

## Requirements 📝

- Python 3.6 or higher
- OpenAI Python SDK

## Installation 🛠️

Clone the repository from GitHub:

```bash
git clone https://github.com/BlakeRhodes/ai.git
```

Navigate to the project directory:

```bash
cd ai
```

Now, build and install the project using setuptools:

```bash
python setup.py install
```

## Configuration ⚙️

Create a `.ai-config` file in your home directory and add your OpenAI API key to it:

```json
{
  "openaiKey": "Your_OpenAI_API_Key"
}
```

## Usage 🚀

Use the command line to run the application:

```bash
ai --key Your_OpenAI_API_Key --temperature 0.0 --shell bash --verbose "Your AI prompt"
```

Command line arguments:

- `--key`: Your OpenAI API key. If not provided, it will try to fetch it from the `.ai-config` file.
- `--temperature`: Controls the randomness of the AI's output. Default value is 0.
- `--shell`: The shell to generate the commands for. Default is `bash`.
- `--verbose`: Turn on logging for the agent's reasoning. Default value is `False`.
- `prompt`: This is the natural language prompt the AI will use to generate the command.

## Example 💡

```bash
ai list all the files in the current directory
```

This will output a bash command to list all the files in the current directory.

## Contributing 🙌

Contributions are always welcome! Please read the contribution guidelines first.

## License 📄

This project is licensed under the terms of the MIT license.

## Disclaimer ⚠️

This project is provided as-is, and might not always work as expected. Always double-check the generated scripts before executing them, especially in production environments!

## Errors 🔍

Please ensure that your OpenAI API Key is correctly inserted and the `.ai-config` file is properly formatted. The `Error` will occur if there are issues with the requests sent to OpenAI. If you encounter any errors, please check your command line arguments or your `.ai-config` file.