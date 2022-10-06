# kivy.uix import 
from kivy.uix.button import Button

# kivy layout import 
from kivy.uix.floatlayout import FloatLayout


from kivy.uix.screenmanager import Screen

# import custom_title_bar
from view.title_bar.custom_title_bar import CustomTitleBar


class HomePage(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


        self.lay_main = FloatLayout()
        # self.lay_main.size_hint = (1,1)

        self.lay_main.add_widget(CustomTitleBar())
        # self.la

        self.lay_main.add_widget(Button(text='HomePage'))



        self.add_widget(self.lay_main)

