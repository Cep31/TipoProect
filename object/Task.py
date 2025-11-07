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

        self._right_answer = self._json['answer']
        self._max_mark = self._json['max_mark']

        self._type = self._json['type']

    def rate(self, answer): # эта функция для проверка ответа
        if self._type == 'test':
            if answer == self._right_answer:
                return self._max_mark
            else:
                return 0
        return 0

    def get_path(self):
        return self._path + '\\cond.png'

    def get_type(self):
        return self._type

    def get_max_mark(self):
        return self._max_mark

    def get_explanation_path(self):
        return self._path + "\\answer.png"