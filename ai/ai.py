import warnings
from string import Template

from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.agents import initialize_agent, AgentType
from langchain.tools import ShellTool

from ai.cli import get_arguments
from ai.loading import LoadingIndicator


def main():
    arguments = get_arguments()
    llm = OpenAI(openai_api_key=arguments.key, temperature=arguments.temperature)
    user_input = ' '.join(arguments.prompt)
    tools = [ShellTool()]

    template = PromptTemplate(
        input_variables=['prompt'],
        template=get_template(arguments.shell)
    )

    indicator = LoadingIndicator()
    indicator.start()

    try:
        steps = LLMChain(llm=llm, prompt=template).run(user_input)
        if arguments.verbose:
            print(f'Here is how I would do it: {steps}')
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=arguments.verbose)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            result = agent.run(steps)
    finally:
        indicator.stop()

    print(result+'\n\n')


def get_template(shell):
    return Template("""
             You are a $shell expert.
             In as few steps as possible, explain how to use $shell to do the following:
             
             {prompt}.
        """).substitute(shell=shell)
