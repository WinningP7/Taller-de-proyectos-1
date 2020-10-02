#actualizar datos firebase
from firebase import firebase 

firebase = firebase.FirebaseApplication("https://halogen-welder-245319.firebaseio.com/",None)

firebase.put('/halogen-welder-245319/Customer/-MIabl7J3hfk-2iK1KOy', 'Direccion', 'Avenida1')
print("Record update")