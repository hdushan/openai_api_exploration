from openai_client import OpenAIClient

client = OpenAIClient()

print("-------------Chaining Example1-------------------")

DELIMITER = "####"
SYSTEM_MESSAGE = f"""
You will be provided with customer service queries. \
The customer service query will be delimited with \
{DELIMITER} characters.
Output a python list of objects, where each object has \
the following format:
    'category': <one of Computers and Laptops, \
    Smartphones and Accessories, \
    Televisions and Home Theater Systems, \
    Gaming Consoles and Accessories, 
    Audio Equipment, Cameras and Camcorders>,
OR
    'products': <a list of products that must \
    be found in the allowed products below>

Where the categories and products must be found in \
the customer service query.
If a product is mentioned, it must be associated with \
the correct category in the allowed products list below.
If no products or categories are found, output an \
empty list.

Allowed products: 

Computers and Laptops category:
TechPro Ultrabook
BlueWave Gaming Laptop
PowerLite Convertible
TechPro Desktop
BlueWave Chromebook

Smartphones and Accessories category:
SmartX ProPhone
MobiTech PowerCase
SmartX MiniPhone
MobiTech Wireless Charger
SmartX EarBuds

Televisions and Home Theater Systems category:
CineView 4K TV
SoundMax Home Theater
CineView 8K TV
SoundMax Soundbar
CineView OLED TV

Gaming Consoles and Accessories category:
GameSphere X
ProGamer Controller
GameSphere Y
ProGamer Racing Wheel
GameSphere VR Headset

Audio Equipment category:
AudioPhonic Noise-Canceling Headphones
WaveSound Bluetooth Speaker
AudioPhonic True Wireless Earbuds
WaveSound Soundbar
AudioPhonic Turntable

Cameras and Camcorders category:
FotoSnap DSLR Camera
ActionCam 4K
FotoSnap Mirrorless Camera
ZoomMaster Camcorder
FotoSnap Instant Camera

Only output the list of objects, with nothing else.
"""
USER_MESSAGE_1 = """
 tell me about the smartx pro phone and \
 the fotosnap camera, the dslr one. \
 Also tell me about your tvs """
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE},
    {"role": "user", "content": f"{DELIMITER}{USER_MESSAGE_1}{DELIMITER}"},
]
category_and_product_response_1 = (
    client.get_completion_from_messages_with_usage_details(messages)
)
print(category_and_product_response_1)

print("-------------Chaining Example2-------------------")

USER_MESSAGE_2 = "my router isn't working"
messages = [
    {"role": "system", "content": SYSTEM_MESSAGE},
    {"role": "user", "content": f"{DELIMITER}{USER_MESSAGE_2}{DELIMITER}"},
]
response = client.get_completion_from_messages_with_usage_details(messages)
print(response)
