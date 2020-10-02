from firebase import firebase 

class FirebaseCrud():

    firebase = firebase.FirebaseApplication("https://halogen-welder-245319.firebaseio.com/",None)



    def firebase_insert(self):
        data = {
            'Nombre Terminal':'Terminal los Andes',
            'Direccion':'Salcedo, Huancayo 12001',
            'Campo 1': 'Valor campo 1'
        }
        result = firebase.post('/halogen-welder-245319/Customer', data)
    
    def firebase_retreive(self):
        result = firebase.get('/halogen-welder-245319/Customer', '')
    
    def firebase_update(self):
        firebase.put('/halogen-welder-245319/Customer/-MIabl7J3hfk-2iK1KOy', 'Direccion', 'Avenida1')
    
    def firebase_delete(self):
        firebase.delete('/halogen-welder-245319/Customer/','-MIabl7J3hfk-2iK1KOy')
        

    

