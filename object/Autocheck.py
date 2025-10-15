from openai import OpenAI
import base64
import os

class Autocheck:
    KEY = "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"

    @staticmethod
    def check(id_image, answer_files):

        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=Autocheck.KEY,
        )

        content = []
        cond = Autocheck.encode_image(fr"{os.getcwd()}\catalog\{id_image}\cond.png")
        content.append({
            "type": "text",
            "text": "Привет, Я решал задачу из ЕГЭ по профильной математике. Сможешь, пожалуйста " +
                                    "проверить её по критериям ЕГЭ по профильной математике и оцени её по баллам. " +
                                    "В первой картинке условие задачу, а во всех остальных - моё решение."
        })
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{cond}"
            }
        })

        for answer in answer_files:
            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{Autocheck.encode_image(fr"{os.getcwd()}\cache\{id_image}\{answer}")}"
                }
            })

        completion = client.chat.completions.create(
            model="google/gemini-2.0-flash-exp:free",
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ]
        )
        return completion.choices[0].message.content

    @staticmethod
    def encode_image(file_path):
        with open(file_path, 'rb') as file:
            encoded = base64.b64encode(file.read()).decode('utf-8')
        return encoded

