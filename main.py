# Core imports from kivy 
from cgitb import text
from unicodedata import name
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

# Windgets imports from kivy
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

from kivy.uix.boxlayout import BoxLayout


# views import
from view.home.home_page import HomePage


# ScreenManager Handler classes
from kivy.uix.screenmanager import (
    Screen,
    ScreenManager
)




class WindowManager(ScreenManager):
    pass


class Main(App):

    def build(self):
        Window.custom_titlebar = 1



        self.sm = ScreenManager()
        self.sm.add_widget(HomePage())



        # data = Window.set_custom_titlebar(Button(text="Set Custom Titlebar"))

        # print('Title status ',data)



        # kv = Builder.load_file("main.kv")
        return self.sm

if __name__ == '__main__':
    Main().run()



