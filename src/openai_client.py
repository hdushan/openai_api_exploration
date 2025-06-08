import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv


class OpenAIClient:
    def __init__(self):
        _ = load_dotenv(find_dotenv())  # read local .env file
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.model = "gpt-3.5-turbo"

    def get_completion(self, prompt):
        messages = [{"role": "user", "content": prompt}]
        response = self.client.chat.completions.create(
            model=self.model, messages=messages, temperature=0
        )
        return response.choices[0].message.content

    def get_completion_from_messages_with_usage_details(
        self, messages, temperature=0, max_tokens=500
    ):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content, response.usage

    def get_moderation(self, input_message):
        response = self.client.moderations.create(
            model="omni-moderation-latest", input=input_message
        )
        for category, result in response.results[0].categories:
            if result:
                print(category + " : " + str(result))
        moderation_output = response.results[0].flagged
        return moderation_output
