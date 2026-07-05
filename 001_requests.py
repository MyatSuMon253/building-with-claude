from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-0"
message = client.messages.create(
    model = model,
    max_tokens = 1000,
    messages = [
        {
            "role": "user",
            "content": "what is quantum computing? Answer in one sentence"
        }
    ]
)
message.content[0].text