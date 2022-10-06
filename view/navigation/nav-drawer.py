# from kivy.uix.boxlayout import BoxLayout



# class NavDrawer(BoxLayout):

#     def __init__(self, **kwargs):

from kivy.lang import Builder
from  kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationLayout

from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from kivy.uix.button import Button

from kivymd.uix.toolbar.toolbar import MDTopAppBar

from kivymd.app import MDApp



from kivy.graphics import Color,Rectangle


KV = '''
MDScreen:

    MDNavigationLayout:

        # MDScreenManager:

        #     MDScreen:

        #         MDTopAppBar:
        #             title: "Navigation Drawer"
        #             elevation: 10
        #             pos_hint: {"top": 1}
        #             md_bg_color: "#e7e4c0"
        #             specific_text_color: "#4a4939"
        #             left_action_items:
        #                 [['menu', lambda x: nav_drawer.set_state("open")]]


        # MDNavigationDrawer:
        #     id: nav_drawer
        #     md_bg_color: "#f7f4e7"

        #     ContentNavigationDrawer:
'''


class ContentNavigationDrawer(MDBoxLayout):
    pass



class CustomNavDrawerWidget(MDNavigationLayout):
    def __init__(self, **kwargs):
        super(CustomNavDrawerWidget, self).__init__(**kwargs)



        self.sm = MDScreenManager()




        self.screen1 = MDScreen()



        # Navigationdrawer items 
        self.nav_drawer = MDNavigationDrawer()
        # self.nav_drawer.id = 'nav_drawer'
        self.nav_drawer.md_bg_color = "#f7f4e7"
        
        self.nav_drawer.add_widget(ContentNavigationDrawer())





        top = MDTopAppBar()
        top.title   = "Custom Navigation"
        top.elevation = 10
        top.pos_hint = {"top": 1}
        top.md_bg_color = "#e7e4c0"
        top.specific_text_color =  "#4a4939"
        top.left_action_items = [['menu', lambda x: self.nav_drawer.set_state("open")]]



        self.screen1.add_widget(top)

        self.sm.add_widget(self.screen1)


        # with self.canvas.before:
        #     Color(0, 1, 0, 1) # green; colors range from 0-1 instead of 0-255


        self.add_widget(self.sm)
        self.add_widget(self.nav_drawer)

# class RootWidget(Widget):

#     def __init__(self, **kwargs):
#         super(RootWidget, self).__init__(**kwargs)


#         # self.size_hint = (1,1)


#         self.add_widget(CustomNavDrawer())




class TestNavigationDrawer(MDApp):
    def build(self):

        root = CustomNavDrawerWidget()

        # wid = RootWidget()

        # with wid.canvas.before:
        #     Color(0, 1, 0, 1)  # green; colors range from 0-1 not 0-255
        #     self.rect = Rectangle(size=wid.size, pos=wid.pos)

        return root


TestNavigationDrawer().run()