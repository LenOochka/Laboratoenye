from cgitb import text
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import os
import sys
from kivy.config import Config
from kivy.core.window import Window
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)

class Convert(App):
    def build(self):
        self.input = "0"
        self.lbl=Label(text = "Выберите конвертор", font_size = 20)
        bl = BoxLayout(orientation = 'vertical')
        gl = GridLayout(cols = 4)
        bl.add_widget(self.lbl)
        bl.add_widget(Button(text="Граммы -> Килограммы/Центнеры/Тонны", on_press = self.switch_on_gr))
        bl.add_widget(Button(text="Рубли -> Доллары/Евро/Фнуты", on_press = self.switch_on_rub))
        bl.add_widget(Button(text="Киломметры -> Мили/Метры/Сантиметры", on_press = self.switch_on_sm))
        bl.add_widget(Button(text="Выход", on_press = self.exit))

        return bl
    def switch_on_gr(self, instance):
        os.system('main4.py')
        sys.exit()
    def switch_on_rub(self, instance):
        os.system('main3.py')
        sys.exit()
    def switch_on_sm(self, instance):
        os.system('main2.py')
        sys.exit()
    def exit(self, instance):
        sys.exit()


if __name__ == "__main__":
    Convert().run()