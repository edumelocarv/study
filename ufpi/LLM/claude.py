import anthropic

def ask(prompt, api_key):

    client = anthropic.Anthropic(
    api_key=api_key,
)
    return client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    ).content[0].text

if __name__ == "__main__":
    message = ask("Onde fica a ufpi?", "key")
    print(message)