import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("https://application-2024-4014c-default-rtdb.asia-southeast1.firebasedatabase.app")
firebase_admin.initialize_app(cred)

db = firestore.client()
print(db)