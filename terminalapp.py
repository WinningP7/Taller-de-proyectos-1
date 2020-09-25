from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


#configurar pantalla
from kivy.config import Config 
#ancho
Config.set("graphics", "width","340")
#largo
Config.set("graphics", "height","640")


class MainWindow(Screen):
    pass    
class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    pass
class FourthWindow(Screen):
    pass
class FifthWindow(Screen):
    pass
class SixthWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv=Builder.load_file("terminalapp.kv")

class Myapp(App):
    def build(self):
        return kv





if __name__ == "__main__":
    Myapp().run()

