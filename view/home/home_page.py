# kivy.uix import 
from kivy.uix.button import Button



from kivy.uix.screenmanager import Screen


class HomePage(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)




        self.add_widget(Button(text='HomePage'  ))

