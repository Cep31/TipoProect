from openai import OpenAI
import base64
import os

class Autocheck:
    @staticmethod
    def check(filepath, id):

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="<OPENROUTER_API_KEY>",
        )

        with open(filepath, "rb") as image_file:
            answer = base64.b64encode(image_file.read()).decode('utf-8')

        with open(fr"{os.getcwd()}\catalog\{id}") as cond_file:
            cond = base64.b64encode(cond_file.read()).decode('utf-8')

        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-exp:free",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Проверь задачу по критериям ЕГЭ по профильной математике"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{cond}"
                            }
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{answer}"
                            }
                        }
                    ]
                }
            ]
        )
        return completion.choices[0].message.content