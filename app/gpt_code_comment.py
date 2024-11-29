"""TODO"""
from pydantic import BaseModel
from typing import Union

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

client = OpenAI()


class ResponseFormat(BaseModel):
    """TODO"""
    commented_code: str
    notes: str


def code_commentor(code: str) -> Union[int, ResponseFormat]:
    """TODO"""
    output = ""
    with open('app/prompt.txt', "r", encoding="utf-8") as f:
        prompt = f.read()
    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": prompt,
            },
            {"role": "user", "content": code},
        ],
        response_format=ResponseFormat,
    )
    output = response.choices[0].message

    if output.parsed:
        output = output.parsed
    else:
        return 0

    return output
