import openai

API_KEY = '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'
openai.api_key = API_KEY

question = input("This is the most basic ChatBot ChatGPT based project.\n Ask anything that I'll answer!\n ->")
answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": question}
    ]
)

print(answer)