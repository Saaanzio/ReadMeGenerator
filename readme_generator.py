def ask(query):
    from openai import OpenAI
    import json

    with open("./secrets.json", "r") as f:
        json_file = json.load(f)

    client = OpenAI(api_key=json_file["api_key"])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": query
            },
        ],
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty= 0.0,
        presence_penalty=0.0
    )
    return response.choices[0].message.content