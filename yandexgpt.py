import requests
import json
from copy import copy

prompt_file = open("prompt.json", "r", encoding="utf-8")
prompt_data = json.load(prompt_file)
prompt_file.close()

api_key = "AQVN14LKrquu9yriAs8QEffnkwnJfLTjej6nDEk4"
catalog_id = ""
modelUri = f"gpt://{catalog_id}/yandexgpt-lite"
url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {api_key}"
}

def get_answer(message):
    prompt = copy(prompt_data)
    prompt["modelUri"] = modelUri
    prompt["messages"][1]["text"] = message
    response = requests.post(url=url, headers=headers, json=prompt)
    return response.json()["result"][0]["alternatives"][0]["message"]["text"]

print(get_answer("lol"))



