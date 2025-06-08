from openai_client import OpenAIClient

client = OpenAIClient()

print("--------------------------------")

response = client.get_completion("What is the capital of France?")
print(response)

response = client.get_completion("Take the letters in lollipop and reverse them")
print(response)

print("--------------------------------")

response = client.get_completion("Take the letters in l-o-l-l-i-p-o-p and reverse them")
print(response)

print("--------------------------------")

messages = [
    {
        "role": "system",
        "content": "You are an assistant who responds in the style of Dr Seuss.",
    },
    {
        "role": "user",
        "content": "write me a very short poem about a happy carrot",
    },
]
response = client.get_completion_from_messages_with_usage_details(
    messages, temperature=1
)
print(response)

print("--------------------------------")
# length
messages = [
    {
        "role": "system",
        "content": "All your responses must be one sentence long.",
    },
    {"role": "user", "content": "write me a story about a happy carrot"},
]
response = client.get_completion_from_messages_with_usage_details(
    messages, temperature=1
)
print(response)

print("--------------------------------")

# combined
messages = [
    {
        "role": "system",
        "content": """You are an assistant who \
responds in the style of Dr Seuss. \
All your responses must be one sentence long.""",
    },
    {"role": "user", "content": "write me a story about a happy carrot"},
]
response = client.get_completion_from_messages_with_usage_details(
    messages, temperature=1
)
print(response)

print("--------------------------------")


messages = [
    {
        "role": "system",
        "content": "You are an assistant who responds in the style of Dr Seuss.",
    },
    {
        "role": "user",
        "content": "write me a very short poem about a happy carrot",
    },
]
response, token_dict = client.get_completion_from_messages_with_usage_details(messages)

print(response)
print(token_dict)

print("--------------------------------")
