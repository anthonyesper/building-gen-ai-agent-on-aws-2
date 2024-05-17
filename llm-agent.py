import transformers
import streamlit as st
from huggingface_hub import InferenceClient
from transformers import CodeAgent, HfEngine

client = InferenceClient(model="https://api-inference.huggingface.co/models/bigcode/starcoder2-3b")


# agent.run(
#     "Could you translate this sentence from French, say it out loud and return the audio.",
#     sentence="Où est la boulangerie la plus proche?",
# )


#Initialize the Agent
agent = CodeAgent(tools=[], add_base_tools=True)

# Define a simple function to use the ReactCodeAgent
def llm_engine(messages, stop_sequences=["Task"]) -> str:
    response = client.chat_completion(messages, stop=stop_sequences, max_tokens=1000)
    answer = response.choices[0].message.content
    print(agent.system_prompt_template)
    return answer


# Streamlit app
st.title("ANSWER BOT")

# User input
user_input = st.text_input("Enter a task for the Answer Bot:")

# Button to trigger the ReactCodeAgent
if st.button("Run AnswerBot"):
    if user_input:
        result = agent.run(user_input)
        st.write("CodeAgent's Response:")
        st.write(result)
    else:
        st.write("Please enter a task for the answer bot.") 

        