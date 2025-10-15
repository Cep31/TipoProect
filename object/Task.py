import json
import os
import tkinter as tk
from tkinter import PhotoImage


class Task:
    def __init__(self, ID):
        self._ID = ID
        self._path = fr'{os.getcwd()}\catalog\{self._ID}'

        with open(self._path + '\\problem.json', 'r') as file:
            self._json = json.load(file)

        self._right_answer = self._json['answer']
        self._max_mark = self._json['max_mark']

        self._answer = 0
        self._mark = 0

        self._type = self._json['type']

    def set_answer(self, ans): # эта функция для сохранения ответа
        self._answer = ans

    def rate(self): # эта функция для проверка ответа
        if self._type == 'test':
            if self._answer == self._right_answer:
                self._mark = self._max_mark

    def get_answer(self):
        return self._answer

    def get_mark(self):
        return self._mark

    def get_photo(self):
        image = PhotoImage(file = self._path + '\\cond.png')
        return image