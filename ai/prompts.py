
AGENT_EXECUTE_PROMPT = """
    Complete the steps above using the terminal. Do it using multiple one liners. Don't open any programs, use
    command line tools only. If you get the same result as before, decide if you should continue or not.
"""

AGENT_PLAN_PROMPT = """
             You are a $shell expert.
             Write a series of steps to complete the following task:
             
             {prompt}.
             
             your steps should be only command line tools, NEVER programs.
             the user does not have any programs they can open.
             so each step should be a command line tool.
             You may use pipes and redirects to combine tools.
             
        """
