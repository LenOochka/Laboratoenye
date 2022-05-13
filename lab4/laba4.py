from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.picker import MDDatePicker

from kivy.config import Config
from kivy.core.window import Window
Config.set('graphics', 'resizable', 0)
Window.size = (320, 568)


class Main(MDApp):
    def build(self):
        return Builder.load_file('data.kv')
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.open()

Main().run()