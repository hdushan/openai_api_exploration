from openai_client import OpenAIClient

client = OpenAIClient()

DELIMITER = "####"
SYSTEM_MESSAGE = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{DELIMITER} characters.
Classify each query into a primary category \
and a secondary category. 
Provide your output in json format with the \
keys: primary and secondary.

Primary categories: Billing, Technical Support, \
Account Management, or General Inquiry.

Billing secondary categories:
Unsubscribe or upgrade
Add a payment method
Explanation for charge
Dispute a charge

Technical Support secondary categories:
General troubleshooting
Device compatibility
Software updates

Account Management secondary categories:
Password reset
Update personal information
Close account
Account security

General Inquiry secondary categories:
Product information
Pricing
Feedback
Speak to a human

"""

print("--------------------------------")

USER_MESSAGE = "I want you to delete my profile and all of my user data"
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE},
    {"role": "user", "content": f"{DELIMITER}{USER_MESSAGE}{DELIMITER}"},
]
response = client.get_completion_from_messages_with_usage_details(messages)
print(response)

print("--------------------------------")

USER_MESSAGE = "Tell me more about your flat screen tvs"
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE},
    {"role": "user", "content": f"{DELIMITER}{USER_MESSAGE}{DELIMITER}"},
]
response = client.get_completion_from_messages_with_usage_details(messages)
print(response)
