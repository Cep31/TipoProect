from openai import OpenAI
import base64

KEY = "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"
MODEL = "mistralai/mistral-small-3.2-24b-instruct:free" # "google/gemini-2.0-flash-exp:free"

def content_generate(cond_path, answer_pathes, task_number):
    content = []
    cond = encode_image(cond_path)
    content.append({
        "type": "text",
        "text": """
        Привет, Я решал задачу из ЕГЭ по профильной математике. Сможешь, пожалуйста проверить её по критериям ЕГЭ по профильной математике и оцени её по баллам.
        В первой картинке условие задачи, вторая картинка описывает критерии оценивания моей задачи, а во всех остальных - моё решение.
        """
    })
    content.append({
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{cond}"
        }
    })

    criteria_path = fr"C:\Users\USER\PycharmProjects\TipoProect\catalog\criteria\{task_number}"
    content.append({
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{criteria_path}"
        }
    })

    for answer in answer_pathes:
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{encode_image(answer)}"
            }
        })

    return content

def check(id_image, answer_pathes, task_number):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=KEY,
    )
    content = content_generate(id_image, answer_pathes, task_number)

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )
    return completion

def encode_image(file_path):
    with open(file_path, 'rb') as file:
        encoded = base64.b64encode(file.read()).decode('utf-8')
    return encoded

response = check(r"C:\Users\USER\PycharmProjects\TipoProect\img.png", [r"C:\Users\USER\Desktop\1234.jpg", r"C:\Users\USER\Desktop\12345.jpg"], 13)
print(response)