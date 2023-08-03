import warnings

from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.agents import initialize_agent, AgentType
from langchain.tools import ShellTool, DuckDuckGoSearchRun
from openai import InvalidRequestError

from ai.cli import arguments

openai = OpenAI(openai_api_key=arguments.key, temperature=arguments.temperature)


def run():
    user_input = ' '.join(arguments.prompt)
    tools = [ShellTool()]
    steps = get_chain().run(user_input)
    if arguments.verbose:
        print(f'Here is how I would do it: {steps}')
    agent = initialize_agent(tools, openai, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=arguments.verbose)

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = agent.run(steps)
    except InvalidRequestError as e:
        result = f'InvalidRequestError: {e}'

    print(result)


def get_chain():
    template = PromptTemplate(
        input_variables=['prompt'],
        template="""
             You are a bash programmer.
             Help the user by generating a script that will do the following:
             {prompt}
        
            answer with the bash script that will do this.
        """
    )
    return LLMChain(llm=openai, prompt=template)
