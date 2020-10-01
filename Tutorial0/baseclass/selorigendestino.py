from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class SelOrigenDestino(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.sub_title = "Seleccion Origen Destino"