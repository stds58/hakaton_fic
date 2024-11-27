
import openai
OPENAI_API_KEY = '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'

client = openai.OpenAI(api_key=OPENAI_API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
