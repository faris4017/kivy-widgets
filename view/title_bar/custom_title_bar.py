# import floatlayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

# import button 
from kivy.uix.button import Button
from kivy.uix.label import Label

class CustomTitleBar(FloatLayout):
    """Class for custom title bar widget"""
    def __init__(self, **kwargs):
        super().__init__()


        self.label_title = Label(text='title_name')


        self.btn_close = Button(text="close")
        self.btn_minimize = Button(text="minimize")
        self.btn_maximize = Button(text="maximize")



        self.lay_action_buttons = BoxLayout()
        self.lay_action_buttons.add_widget(self.btn_minimize)
        self.lay_action_buttons.add_widget(self.btn_maximize)
        self.lay_action_buttons.add_widget(self.btn_close)



        self._lay_main = FloatLayout()
        self._lay_main.add_widget(self.label_title)
        self._lay_main.add_widget(self.lay_action_buttons)

        self.add_widget(self._lay_main)