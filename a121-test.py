import os

from ai21 import AI21Client
from ai21.models.chat import ChatMessage

client = AI21Client(api_key=os.environ.get("AI21_API_KEY"))

messages = [
    ChatMessage(
        content="How long does it take to finish acturial exams?",
        role="user",	
    ),
]

response = client.chat.completions.create(
  model="jamba-instruct-preview",
  messages=messages,
  max_tokens=1024,
)

agent_response = response.choices[0].message.content
print(agent_response)