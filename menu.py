from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

class UI(ScreenManager):
    pass 

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.key = None
        self.url = 'wwww.api.com/?'
        

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepPurple'
        Builder.load_file('estilo.kv')

        return UI()
    
def change_style(Self, checked, value):
    if value:
        Self.theme_cls.theme_style = 'Dark'
    else:
        Self.theme_cls.theme_style = 'Light'



if __name__ =="__main__":
    MainApp().run()