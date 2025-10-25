import json
import os

class Task:
    def __init__(self, ID):
        self._ID = ID
        self._path = fr'{os.getcwd()}\catalog\{self._ID}'

        if not os.path.exists(self._path):
            self._ID = "01_01_001"
            self._path = fr'{os.getcwd()}\catalog\01_01_001'

        with open(self._path + '\\problem.json', 'r') as file:
                self._json = json.load(file)

        self._right_answer = self._json['answer']
        self._max_mark = self._json['max_mark']

        self._mark = 0

        self._type = self._json['type']

    def rate(self, answer): # эта функция для проверка ответа
        if self._type == 'test':
            if answer == self._right_answer:
                self._mark = self._max_mark

    def get_answer(self):
        return self._answer

    def get_mark(self):
        return self._mark

    def get_path(self):
        return self._path + '\\cond.png'

    def get_type(self):
        return self._type