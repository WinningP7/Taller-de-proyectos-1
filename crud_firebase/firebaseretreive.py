#obtener datos firebase
from firebase import firebase 

firebase = firebase.FirebaseApplication("https://halogen-welder-245319.firebaseio.com/",None)
result = firebase.get('/halogen-welder-245319/Customer', '')
print(result)