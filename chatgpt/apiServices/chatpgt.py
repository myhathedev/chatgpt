from openai import OpenAI
client = OpenAI()


def fetch_chatgpt(prompt):
    # Make the API request
    print('fetch')
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a scientist assistant"},
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    # Extract and return the assistant's reply
    return answer
