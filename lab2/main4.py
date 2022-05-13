from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os
import sys

from kivy.core.window import Window
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.t = Label(text="Граммы")
        self.kg = Label(text="Килограммы")
        self.cent = Label(text="Центнеры")
        self.input_data = TextInput(hint_text="Введите значение (тонны)", multiline=False)
        self.input_data.bind(text=self.on_text)

    def build(self):
        box = BoxLayout(orientation="vertical")
        box.add_widget(Button(text="Назад", on_press=self.switch_back))
        box.add_widget(self.input_data)
        box.add_widget(self.t)
        box.add_widget(self.kg)
        box.add_widget(self.cent)

        return box
    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.kg.text = "Килограммы: " + str(float(data) / 1000)
            self.cent.text = "Центнеры: " + str(float(data) / 100000)
            self.t.text = "Тонны: " + str(float(data) / 1000000)
        else:
            self.input_data.text = "0"

    def switch_back(self, instance):
        os.system('main.py')
        sys.exit()
if __name__ == '__main__':
    MyApp().run()