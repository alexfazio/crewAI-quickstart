import os
from crewai import Agent, Task, Crew, Process
from decouple import config
from textwrap import dedent
from langchain_community.chat_models import ChatOpenAI
# ↑ uncomment to use OpenAI's API
# from langchain_groq import ChatGroq
# ↑ uncomment to use Groq's API
# from langchain_anthropic import ChatAnthropic
# ↑ uncomment to use Antrhopic's API

# Add API key within `./.env.example.example.example.example` file
os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
# ↑ uncomment to use OpenAI's API
# os.environ["GROQ_API_KEY"] = config("GROQ_API_KEY")
# ↑ uncomment to use Groq's API
# os.environ["ANTHROPIC_API_KEY"] = config("ANTHROPIC_API_KEY")
# ↑ uncomment to use Anthropic's API

print("## Welcome to the YOUR_CREW_NAME")
print('-------------------------------------------')
var_1 = input(dedent((
    f"""What is the <var_1> to pass to your crew?\n
    """))),
var_2 = input(dedent((
    f"""What is the <var_1> to pass to your crew?\n
    """))),
var_3 = input(dedent((
    f"""What is the <var_1> to pass to your crew?\n
    """))),
print("-------------------------------")

# Agent Definitions

agent_1 = Agent(
    role=dedent((
        f"""
        Mr. White
        """)),
        # ↑ Defines the agent's function within the crew. It determines the kind of tasks the agent is best suited for.
    backstory=dedent((
        f"""
        Provides context to the agent's role and goal, enriching the interaction and collaboration dynamics.
        """)),
    goal=dedent((
        f"""
        The individual objective that the agent aims to achieve. It guides the agent's decision-making process.
        """)),
    allow_delegation=True,
    verbose=True,
    # ↑ Whether the agent execution should be in verbose mode
    max_iter=3,
    # ↑ maximum number of iterations the agent can perform before being forced to give its best answer
    max_rpm=3,
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.8)
    # ↑ uncomment to use OpenAI API + "gpt-4"
    # llm=ChatGroq(temperature=0.8, model_name="mixtral-8x7b-32768"),
    # ↑ uncomment to use Groq's API + "llama3-70b-8192"
    # llm=ChatGroq(temperature=0.6, model_name="llama3-70b-8192"),
    # ↑ uncomment to use Groq's API + "mixtral-8x7b-32768"
    # llm = ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8),
    # ↑ uncomment to use Anthropic's API + "claude-3-opus-20240229"
)

agent_2 = Agent(
    role=dedent((
        f"""
        Mr. Orange
        """)),
        # Defines the agent's function within the crew. It determines the kind of tasks the agent is best suited for.
    backstory=dedent((
        f"""
        Provides context to the agent's role and goal, enriching the interaction and collaboration dynamics.
        """)),
    goal=dedent((
        f"""
        The individual objective that the agent aims to achieve. It guides the agent's decision-making process.
        """)),
    allow_delegation=True,
    verbose=True,
    # ↑ Whether the agent execution should be in verbose mode
    max_iter=3,
    # ↑ maximum number of iterations the agent can perform before being forced to give its best answer
    max_rpm=3,
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.8)
    # ↑ uncomment to use OpenAI API + "gpt-4"
    # llm=ChatGroq(temperature=0.8, model_name="mixtral-8x7b-32768"),
    # ↑ uncomment to use Groq's API + "llama3-70b-8192"
    # llm=ChatGroq(temperature=0.6, model_name="llama3-70b-8192"),
    # ↑ uncomment to use Groq's API + "mixtral-8x7b-32768"
    # llm = ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8),
    # ↑ uncomment to use Anthropic's API + "claude-3-opus-20240229"
)

agent_3 = Agent(
    role=dedent((
        f"""
        Mr. Pink
        """)),
        # ↑ Defines the agent's function within the crew. It determines the kind of tasks the agent is best suited for.
    backstory=dedent((
        f"""
        Provides context to the agent's role and goal, enriching the interaction and collaboration dynamics.
        """)),
    goal=dedent((
        f"""
        The individual objective that the agent aims to achieve. It guides the agent's decision-making process.
        """)),
    allow_delegation=True,
    verbose=True,
    # ↑ Whether the agent execution should be in verbose mode
    max_iter=3,
    # ↑ maximum number of iterations the agent can perform before being forced to give its best answer
    max_rpm=3,
    llm=ChatOpenAI(model_name="gpt-4", temperature=0.8)
    # ↑ uncomment to use OpenAI API + "gpt-4"
    # llm=ChatGroq(temperature=0.8, model_name="mixtral-8x7b-32768"),
    # ↑ uncomment to use Groq's API + "llama3-70b-8192"
    # llm=ChatGroq(temperature=0.6, model_name="llama3-70b-8192"),
    # ↑ uncomment to use Groq's API + "mixtral-8x7b-32768"
    # llm = ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8),
    # ↑ uncomment to use Anthropic's API + "claude-3-opus-20240229"
)

# Task Definitions

task_1 = Task(
    description=dedent((
        f"""
        A clear, concise statement of what the task entails.
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """)),
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like.
        """)),
  agent=agent_1,
)

task_2 = Task(
    description=dedent((
        f"""
        A clear, concise statement of what the task entails.
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """)),
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like.
        """)),
    agent=agent_2,
    context=[task_1],
    # ↑ specify which task's output should be used as context for subsequent tasks
)

task_3 = Task(
    description=dedent((
        f"""
        A clear, concise statement of what the task entails.
        ---
        VARIABLE 1: "{var_1}"
        VARIABLE 2: "{var_2}"
        VARIABLE 3: "{var_3}"
        Add more variables if needed...
        """)),
    expected_output=dedent((
        f"""
        A detailed description of what the task's completion looks like.
        """)),
    agent=agent_3,
    context=[task_1, task_2],
    # ↑ specify which task's output should be used as context for subsequent tasks
)

def main():
    # Instantiate your crew with a sequential process
    crew = Crew(
        agents=[agent_1, agent_2, agent_3],
        tasks=[task_1, task_2, task_3],
        verbose=True,  # You can set it to True or False
        # ↑ indicates the verbosity level for logging during execution.
        process=Process.hierarchical,
        # ↑ the process flow that the crew will follow (e.g., sequential, hierarchical).
        manager_llm=ChatOpenAI(model_name="gpt-4", temperature=0.8),
        # ↑ uncomment to use OpenAI API + "gpt-4"
        # manager_llm=ChatGroq(temperature=0.8, model_name="mixtral-8x7b-32768"),
        # ↑ uncomment to use Groq's API + "llama3-70b-8192"
        # manager_llm=ChatGroq(temperature=0.6, model_name="llama3-70b-8192"),
        # ↑ uncomment to use Groq's API + "mixtral-8x7b-32768"
        # manager_llm=ChatAnthropic(model='claude-3-opus-20240229', temperature=0.8),
        # ↑ uncomment to use Anthropic's API + "claude-3-opus-20240229"
        output_log_file = "./output.log"
        )

    result = crew.kickoff()
    print(dedent(f"""\n\n########################"""))
    print(dedent(f"""## Here is your custom crew run result:"""))
    print(dedent(f"""########################\n"""))
    print(result)

if __name__ == "__main__":
    main()
