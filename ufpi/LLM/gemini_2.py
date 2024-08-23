import google.generativeai as genai

def ask(prompt, api_key):

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    return  model.generate_content(prompt).text


if __name__ == "__main__":
    print(ask("Me fale tudo sobre voce.", "key"))