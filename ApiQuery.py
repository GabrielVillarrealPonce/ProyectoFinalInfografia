from openai import OpenAI

def query_api(prompt):      
    client = OpenAI(api_key="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",
    base_url="https://openrouter.ai/api/v1")

    chat = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {
                "role": "user",
                "content":prompt
            }
        ]
    )
    print(chat.choices[0].message.content)
    return chat.choices[0].message.content

#query_api("Cuántas 'r' tiene la palabra para Arrollador")