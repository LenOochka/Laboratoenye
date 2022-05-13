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
        self.dol = Label(text="Доллары")
        self.eu = Label(text="Евро")
        self.ft = Label(text="Фунты")
        self.input_data = TextInput(hint_text="Введите значение (руб)", multiline=False)
        self.input_data.bind(text=self.on_text)

    def build(self):
        box = BoxLayout(orientation="vertical")
        box.add_widget(Button(text="Назад", on_press=self.switch_back))
        box.add_widget(self.input_data)
        box.add_widget(self.dol)
        box.add_widget(self.eu)
        box.add_widget(self.ft)

        return box
    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.dol.text = "Доллары: " + str(float(data) * 0.0141)
            self.eu.text = "Евро: " + str(float(data) * 0.0134)
            self.ft.text = "Фунты: " + str(float(data) * 0.0113)
        else:
            self.input_data.text = "0"

    def switch_back(self, instance):
        os.system('main.py')
        sys.exit()
if __name__ == '__main__':
    MyApp().run()