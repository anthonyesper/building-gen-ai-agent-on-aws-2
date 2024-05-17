import transformers
import inspect
import streamlit as st

# Show the path of the transformers package
print("Transformers package path:", transformers.__file__)

# Example: Show the path of the HfEngine class
from transformers import HfEngine, Toolbox
print("HfEngine class path:", inspect.getfile(HfEngine))

# Example: Show the path of the CodeAgent class
from transformers import CodeAgent
print("CodeAgent class path:", inspect.getfile(CodeAgent))

# Initialize the HfEngine
engine = HfEngine()

# Initialize the Toolbox with default tools
toolbox = Toolbox(tools=[], add_base_tools=True)

# Define a simple function to use the ReactCodeAgent
def use_react_code_agent(user_input):
    messages = [
        {"role": "user", "content": user_input}
    ]
    tools = list(toolbox.tools.values())  # Get the list of tools from the toolbox
    agent = CodeAgent(tools, llm_engine=engine)
    response = agent.run(task=user_input, document="This is a sample document for the DocumentQuestionAnsweringTool.")
    return response

# Streamlit app
st.title("Transformers ReactCodeAgent with Streamlit")

# User input
user_input = st.text_input("Enter a task for the CodeAgent:")

# Button to trigger the ReactCodeAgent
if st.button("Run CodeAgent"):
    if user_input:
        result = use_react_code_agent(user_input)
        st.write("CodeAgent's Response:")
        st.write(result)
    else:
        st.write("Please enter a task for the CodeAgent.") 