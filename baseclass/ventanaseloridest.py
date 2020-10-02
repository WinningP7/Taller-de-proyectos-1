from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
#MDDialog
from kivymd.uix.dialog import MDDialog
#MDFlatButton
from kivymd.uix.button import MDFlatButton
#web scraping
from facebook_scraper import get_posts
#Tiempo
import time

from kivy.properties import StringProperty
from kivymd.uix.list import OneLineAvatarListItem

class Item(OneLineAvatarListItem):
    divider = None 
    source = StringProperty()

class VentanaSelOriDest(Screen):

    #Builder.load_string(kv)
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        #agregar widget
        self.add_trip_dialog = None
        self.sub_title = "Seleccionar origen y destino"
        

    def show_alert_dialog(self):
        post_facebook = PostFacebook()
        #pub es una lista que continene todo los titulos de publicaciones
        pub = post_facebook.obtener_post()
        contador_pub = len(pub)
        
        self.my_dialog = MDDialog(title = "Alerta Perú" ,
                                type="simple",
                                items=[
                                    Item(text=pub[0]),
                                    Item(text=pub[1]),
                                ],
                                
                                size_hint=[.5,.5],buttons=[
                                    MDFlatButton(text="OK",on_release=self.close_dialog)
                                    ,
                                ],
                                )
        self.my_dialog.open()
    
    def close_dialog(self, button):
        self.my_dialog.dismiss()


class PostFacebook():
    #nombre_facebook = "alertaperu2018"

    def obtener_post(self):
        
        # try:
        #     for post in get_posts(nombre_facebook):
        #         if "time" in post:
        #             fechas_horas = post["time"]
        #             fechas_horas_cad = str(fechas_horas)
        #             fecha_cad = fechas_horas_cad.split()
        #             fecha_actual_pc = time.strftime("%Y-%m-%d")
        #             if fecha_cad[0] == str(fecha_actual_pc):
        #                 #llamando a funcion "cadena_post"
        #                 titulos_post = cadena_post(post)
        #                 contador_titulos_post = contador_titulos_post + 1
                        
        #                 print("[*] %s--->%s"%(titulos_post[0],titulos_post[1]))
        #         else:
        #             print("No tiene llave la publicacion")
        # except:
        #     print("Error")
        #return titulos_post[0]
        save_titulos = []
        for post in get_posts("alertaperu2018"):
            if "time" in post:
                fechas_horas = post["time"]
                fechas_horas_cad = str(fechas_horas)
                fecha_cad = fechas_horas_cad.split()
                fecha_actual_pc = time.strftime("%Y-%m-%d")
                if fecha_cad[0] == str(fecha_actual_pc):
                    #llamando a funcion "cadena_post"
                    titulos_post = self.cadena_post(post)
                    save_titulos.append(titulos_post[0])
                    #contador_titulos_post = contador_titulos_post + 1
                    
                    #print("[*] %s--->%s"%(titulos_post[0],titulos_post[1]))
            else:
                print("No tiene llave la publicacion")
        return save_titulos
    
    def cadena_post(self, post_recv):
        lista_titulos = ""
        if "text" in post_recv and "post_url" in post_recv:
            valor_text = post_recv["text"]
            valor_post_url = post_recv["post_url"]
            for letra_lista_tit in str(valor_text):
                if letra_lista_tit != "\n":
                    lista_titulos = lista_titulos + letra_lista_tit
                else: 
                    break
        else:
            print("llave no encontrada")
        return lista_titulos, str(valor_post_url)
    
    
        
    
    

        
