from settings import get_settings
from openai import OpenAI
# client = OpenAI()




if __name__ == "__main__":
    # Example usage of get_settings
    settings = get_settings()
    client = OpenAI(
        api_key = settings.OPENAI_API_KEY,
    )

    response = client.responses.create(
        model="gpt-4.1-nano-2025-04-14",
        input="Qual a época do plantio do tomate cereja?"
    )

    print(response.output_text)


# settings = get_settings()
# print(settings.OPENAI_API_KEY)