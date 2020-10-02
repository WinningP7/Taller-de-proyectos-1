
from kivymd.app import MDApp 
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


from baseclass.ventanaprincipal import VentanaPrincipal
from baseclass.ventanaseloridest import VentanaSelOriDest
from baseclass.ventanaterminales import VentanaTerminales
from baseclass.ventanaempresas import VentanaEmpresas
from baseclass.ventanabus import VentanaBus

class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        self.title = "MI PRIMERA APP"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("main.kv")

MyApp().run()