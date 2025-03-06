import firebase_admin
from firebase_admin import credentials
from Inventory import Inventory

cred = credentials.Certificate("C:/Users/nicho/Documents/Programming/College/CSE310-WI25/cloud_inventory/cloud-demo-47f8d-firebase-adminsdk-fbsvc-1d32af7619.json")
firebase_admin.initialize_app(cred)

