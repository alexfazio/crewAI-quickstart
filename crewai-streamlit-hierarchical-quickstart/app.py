import streamlit as st
import sys
from crewai import Agent, Task, Crew, Process
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatOpenAI
from stream import StreamToStreamlit
from textwrap import dedent


def main():
    st.sidebar.title('Customization')
    api = st.sidebar.selectbox(
        'Choose an API',
        ['Groq', 'OpenAI', 'Anthropic']
    )

    api_key = st.sidebar.text_input('Enter API Key', 'gsk-')

    temp = st.sidebar.slider("Model Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

    if api == 'Groq':
        model = st.sidebar.selectbox(
            'Choose a model',
            ['llama3-70b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it']
        )

        llm = ChatGroq(
            temperature=temp,
            model_name=model,
            groq_api_key=api_key
        )

    if api == 'OpenAI':
        model = st.sidebar.selectbox(
            'Choose a model',
            ['gpt-4-turbo', 'gpt-4-1106-preview', 'gpt-3.5-turbo-0125']
        )

        llm = ChatOpenAI(
            temperature=temp,
            openai_api_key=api_key,
            model_name=model
        )

    if api == 'Anthropic':
        model = st.sidebar.selectbox(
            'Choose a model',
            ['claude-3-opus-20240229', 'claude-3-sonnet-20240229', 'claude-3-haiku-20240307']
        )

        llm = ChatAnthropic(
            temperature=temp,
            anthropic_api_key=api_key,
            model_name=model
        )

    # Streamlit UI
    st.title('My New Crew')
    multiline_text = """
    This crew does something
    """

    st.markdown(multiline_text, unsafe_allow_html=True)

    # Display the Groq logo

    spacer, col = st.columns([5, 1])
    with col:
        st.image('crewai-logo.png')

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
        llm=llm
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
        llm=llm
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
        llm=llm
    )

    var_1 = st.text_input("Variable 1:")
    var_2 = st.text_input("Variable 2:")
    var_3 = st.text_input("Variable 3:")

    if var_1 and var_2 and var_3 and api_key:
        if st.button("Start"):

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

            # Instantiate your crew with a sequential process
            crew = Crew(
                agents=[agent_1, agent_2, agent_3],
                tasks=[task_1, task_2, task_3],
                verbose=True,  # You can set it to True or False
                # ↑ indicates the verbosity level for logging during execution.
                process=Process.hierarchical,
                # ↑ the process flow that the crew will follow (e.g., sequential, hierarchical).
                manager_llm=llm,
                output_log_file="./output.log"
            )

            with st.spinner("Generating..."):
                # Save the original stdout so we can restore it later
                original_stdout = sys.stdout
                sys.stdout = StreamToStreamlit(st)

                result = ""
                result_container = st.empty()
                for delta in crew.kickoff():
                    result += delta  # Assuming delta is a string, if not, convert it appropriately
                    result_container.markdown(result)


if __name__ == "__main__":
    main()
