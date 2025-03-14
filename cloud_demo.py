import firebase_admin
from firebase_admin import credentials, firestore
from Inventory import Inventory
from Item import Item

def show_menu():
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Edit Item")
    print("4. Display Inventory")
    print("5. Exit")
    try:
        return int(input("Enter a choice: "))
    except:
        print("Invalid choice")
        show_menu()


def start_inventory(inv : Inventory, ref : object):
    
    choice = show_menu()
    #TODO: Load from cloud db
    if choice == 1:
        name = input("Enter item name: ")
        qty = input("Enter item quantity: ")
        
        inv.add_item(Item(name,qty),ref)
        
    elif choice == 2:
        id = int(input("Enter item id: "))
        search = inv.get_item_id(id)
        if search is None:
            print("Item not found")
            return
        inv.remove_item(search,ref)

    elif choice == 3:
        try:
            item = int(input("Enter item id: "))
        except:
            print("Invalid id")
            return
        search = inv.get_item_id(item)
        if search is None:
            print("Item not found")
            return
        
        inv.update_item(search,ref)

    elif choice == 4:
        print(inv.__str__())
    elif choice == 5:
        return
    start_inventory(inv,ref)

#set credentials for access
cred = credentials.Certificate("C:/Users/nicho/Documents/Programming/College/CSE310-WI25/cloud_inventory/cloud-inventory/cloud-demo-47f8d-firebase-adminsdk-fbsvc-1d32af7619.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

inv_name = input("Enter inventory name: ")
doc_ref = db.collection(inv_name)

doc = doc_ref.get()
inv = Inventory(inv_name,[])
if any(doc):
    inv.from_dict(self=inv,d=doc,name=inv_name)
else:
    print("Creating new inventory")
start_inventory(inv,doc_ref)