import time
from io import BytesIO

from PIL import Image
from openai import OpenAI
import base64

KEY = "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"
#KEY = "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"
MODEL = "openrouter/polaris-alpha" # "google/gemini-2.0-flash-exp:free"
# openrouter/polaris-alpha
# mistralai/mistral-small-3.2-24b-instruct:free

def content_generate(cond_path, answer_pathes, task_number):
    content = []
    content.append({
        "type": "text",
        "text": """
        Привет, Я решал задачу из ЕГЭ по профильной математике. Сможешь, пожалуйста проверить её по критериям ЕГЭ по профильной математике и оцени её по баллам.
        В первой картинке условие задачи, вторая картинка описывает критерии оценивания моей задачи, а во всех остальных - моё решение.
        Также, поставь одну цифру - количество моих баллов в самый последний символ твоего ответа, так мне будет легче это найти
        """
    })
    content.append({
        "type": "image_url",
        "image_url": {
            "url": img_to_base64_str(cond_path, 'png')
        }
    })

    criteria_path = fr"C:\Users\USER\PycharmProjects\TipoProect\catalog\criteria\{task_number}.png"
    content.append({
        "type": "image_url",
        "image_url": {
            "url": img_to_base64_str(criteria_path, 'png')
        }
    })

    for answer in answer_pathes:
        content.append({
            "type": "image_url",
            "image_url": {
                "url": img_to_base64_str(answer, 'jpeg')
            }
        })

    return content

# долгая функция
# def check(id_image, answer_pathes, task_number):
#     client = OpenAI(
#         base_url="https://openrouter.ai/api/v1",
#         api_key=KEY,
#     )
#     content = content_generate(id_image, answer_pathes, task_number)
#
#     completion = client.chat.completions.create(
#         model=MODEL,
#         messages=[
#             {
#                 "role": "user",
#                 "content": content
#             }
#         ]
#     )
#     return completion.choices[0].message.content

def check(id_image, answer_pathes, task_number):
    time.sleep(5)
    return "13213123123"

def img_to_base64_str(img_path: str, type: str):
    img = Image.open(img_path)
    img.thumbnail((500, 500), Image.Resampling.LANCZOS)
    buffered = BytesIO()
    img.save(buffered, format=type.upper())
    buffered.seek(0)
    img_byte = buffered.getvalue()
    img_str = f"data:image/{type};base64,{base64.b64encode(img_byte).decode()}"
    return img_str
