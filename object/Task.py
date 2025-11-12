import json
import os

class Task:
    def __init__(self, ID):
        self._ID = ID
        self._path = fr'{os.getcwd()}\catalog\{self._ID}'

        if not os.path.exists(self._path):
            print(f"Path {self._path} not found")
            self._ID = "01_01_001"
            self._path = fr'{os.getcwd()}\catalog\01_01_001'

        with open(self._path + '\\problem.json', 'r') as file:
                self._json = json.load(file)

        self._type = self._json['type']

        if self._type == "test":
            self._right_answer = self._json['answer']
        self._max_mark = self._json['max_mark']

    def rate_detailed(self, answers_paths): # эта функция для проверка ответа
        if not answers_paths:
            return 'где картинки?'

        #answer = check(аргументы)
        #return answer
        return f'Плохо: -1/{self._max_mark}'

    def rate_test(self, answer):
        if not answer:
            return 0

        if answer == self._right_answer:
            return self._max_mark
        else:
            return 0

    def get_path(self):
        return self._path + '\\cond.png'

    def get_type(self):
        return self._type

    def get_max_mark(self):
        return self._max_mark

    def get_explanation_path(self):
        return self._path + "\\answer.png"

    def get_task_number(self):
        return int(self._ID[:1])