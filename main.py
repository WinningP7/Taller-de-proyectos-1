import kivy 
from kivy.app import App 
from  kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

#configurar pantalla
from kivy.config import Config 
#ancho
Config.set("graphics", "width","340")
#largo
Config.set("graphics", "height","640")

class MainWid(ScreenManager):
    #definiendo metodo init con parametros en diccionario
    def __init__(self, **kwarg):
        super(MainWid, self).__init__()
        self.StartWid = StartWid()
        wid = Screen(name = "start")
        wid.add_widget(self.StartWid)
        self.add_widget(wid)

class StartWid(BoxLayout):
    pass

class MainApp(App):
    title = "TIME BUS"
    def build(self):
        return MainWid()



if __name__ == "__main__":
    MainApp().run()
