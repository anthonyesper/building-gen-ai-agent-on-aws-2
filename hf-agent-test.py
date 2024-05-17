import transformers
import inspect
import streamlit as st
from transformers import HfEngine, Toolbox
from transformers import CodeAgent


# Initialize the HfEngine
engine = HfEngine()

# Initialize the Toolbox with default tools
toolbox = Toolbox(tools=[], add_base_tools=True)

# Define a simple function to use the ReactCodeAgent
def RunCodeAgent(user_input):
    messages = [
        {"role": "user", "content": user_input}
    ]
    tools = list(toolbox.tools.values())  # Get the list of tools from the toolbox
    agent = CodeAgent(tools, llm_engine=engine)
    response = agent.run(task=user_input)
    return response

# Streamlit app
st.title("Transformers ReactCodeAgent with Streamlit")

# User input
user_input = st.text_input("Enter a task for the CodeAgent:")

# Button to trigger the ReactCodeAgent
if st.button("Run CodeAgent"):
    if user_input:
        result = RunCodeAgent(user_input)
        st.write("CodeAgent's Response:")
        st.write(result)
    else:
        st.write("Please enter a task for the CodeAgent.") 