from openai import OpenAI
from dotenv import load_dotenv

# Load API Keys
load_dotenv()

# initialize OpenAI API
client = OpenAI()

# Set a specific role, behavior, tone, etc.
# System message is active throughout the whole converstation
system_prompt = """You are a helpful assistant speaking Pirate English"""

completion = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "How to learn fast?"},
    ],
)

print(completion.choices[0].message.content)
