import time
from io import BytesIO

from PIL import Image
from openai import OpenAI
import base64

with open('.env') as f: KEY = f.read()

#MODEL = "openrouter/polaris-alpha" # платно
#MODEL = "google/gemini-2.0-flash-exp:free" # больше не работает
#MODEL = "openrouter/hunter-alpha" # стабильно отвечает, но не видит картинки
MODEL = "openrouter/healer-alpha" # решает медленно, иногда бракует ответ    ------ пока что лучший
#MODEL = "qwen/qwen2.5-vl-32b-instruct:free"
#MODEL = "mistralai/mistral-small-3.1-24b-instruct:free"
#MODEL = "allenai/molmo-2-8b:free"
#MODEL = "sourceful/riverflow-v2-max-preview"
#MODEL = "nvidia/nemotron-nano-12b-v2-vl:free"

def explanation_content_generate(cond_path, answer_pathes, task_number):
    content = []
    content.append({
        "type": "text",
        "text": """
        Привет, Я решал задачу из ЕГЭ по профильной математике. Сможешь, пожалуйста проверить её по критериям ЕГЭ по профильной математике и оцени её по баллам.
        В первой картинке условие задачи, вторая картинка описывает критерии оценивания моей задачи, а во всех остальных - моё решение.
        Также, поставь одну цифру - количество моих баллов в САМЫЙ ПОСДЛЕДНИЙ символ твоего ответа, это ОЧЕНЬ важно, так мне будет легче это найти.
        
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

def answer_content_generate(cond_path):
    content = []
    content.append({
        "type": "text",
        "text": """
            Привет, помоги решить задачу(её условие в картинке). Решай с полным оформлением. И напиши ПОСЛЕДНИМ символом число '0' ОБЯЗАТЕЛЬНО
            """
    })

    content.append({
        "type": "image_url",
        "image_url": {
            "url": img_to_base64_str(cond_path, 'png')
        }
    })

    return content

# долгая функция
def check(cond_path, answer_pathes, task_number):
    if not answer_pathes:
        print("GENERATE ANSWER")
        content = answer_content_generate(cond_path)
    else:
        print("GENERATE EXPLANATION")
        content = explanation_content_generate(cond_path, answer_pathes, task_number)

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=KEY,
    )

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )

    return completion.choices[0].message.content

# def check(id_image, answer_pathes, task_number):
#     time.sleep(5)
#     return "13213123123"

def img_to_base64_str(img_path: str, type: str):
    img = Image.open(img_path)
    img.thumbnail((600, 600), Image.Resampling.LANCZOS)
    buffered = BytesIO()
    img.save(buffered, format=type.upper())
    buffered.seek(0)
    img_byte = buffered.getvalue()
    img_str = f"data:image/{type};base64,{base64.b64encode(img_byte).decode()}"
    return img_str
