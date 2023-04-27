
import requests

def apites():
    headers = {
        'authority': 'api.aiprm.com',
        'accept': '*/*',
        'accept-language': 'ja',
        'content-type': 'application/json',
        'origin': 'https://chat.openai.com',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    json_data = {
        'UsageTypeNo': 2,
        'User': {
            'ExternalID': 'user-xtV1ht5CXcXz1IkkRPSW8Ue4',
            'ExternalSystemNo': 1,
            'UserStatusNo': 1,
            'UserLevelNo': 64,
            'UserFootprint': '01-bc0f8e440a12fb867a83305e001a865e',
            'MaxNewPrivatePromptsAllowed': 2,
            'MaxNewPublicPromptsAllowed': 1,
            'IsLinked': True,
        },
    }

    response = requests.post('https://api.aiprm.com/api3/Prompts/1796267657000120320/Use', headers=headers, json=json_data)
    print(response)



import json
import os
import re

def sanitize(string):
    string = string.replace('&', 'and')
    string = re.sub('[^a-zA-Z0-9 \-,]', '', string)
    string = string.strip()
    return string

def file_content_from_prompt(prompt):
    prompt.Teaser = prompt.Teaser.strip()
    return f"""AuthorName: {prompt.AuthorName}
AuthorURL: {prompt.AuthorURL}

Title: {prompt.Title}
Category: {prompt.Category}
Teaser: {prompt.Teaser}

Community: {prompt.Community}
CreationTime: {prompt.CreationTime}
Help: {prompt.Help}
ID: {prompt.ID}
PromptHint: {prompt.PromptHint}
PromptPackageID: {prompt.PromptPackageID}

Prompt:
{prompt.Prompt}"""

with open('https://api.aiprm.com/api2/Prompts?Community=&Limit=10&Offset=0&OwnerExternalID=user-Sym2oNwW2gUBywbi1gqkKPyB&OwnerExternalSystemNo=1&SortModeNo=2') as file:
    prompts = json.load(file)

for prompt in prompts:
    topic, _ = prompt.Community.split('-', 1)
    path = f"prompts/{topic}/{prompt.Category}"
    name = sanitize(prompt.Title).lower()
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/{name}.txt", 'w') as file:
        file.write(file_content_from_prompt(prompt))



if __name__ == "__main__":
    import pdb;pdb.set_trace()
    print('end')
    