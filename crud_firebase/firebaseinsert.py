from firebase import firebase 

firebase = firebase.FirebaseApplication("https://halogen-welder-245319.firebaseio.com/",None)

data ={
    'Nombre Terminal':'Terminal los Andes',
    
    'Direccion':'Salcedo, Huancayo 12001',
    'Campo 1': 'Valor campo 1'
    

}

result = firebase.post('/halogen-welder-245319/Customer', data)

print(result)