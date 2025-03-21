from typing import List
from firebase_admin import firestore
from Item import Item

class Inventory:
    def __init__(self,name : str,items : List[Item]):
        self.name = name
        self.items = items

    def __str__(self):
        summ = f"Inventory: {self.name}\n"
        for i in self.items:
            summ += f"{i}\n"
        return summ
    
    @staticmethod
    def from_dict(self,d : object, name : str):
        self.name = name
        self.items = [] #empty init
        for i in d:
            item = Item(i.get('name'),i.get('qty'))
            item.id = i.get('id')
            if item.id >= Item.nextId: #update nextId if id is greater
                Item.nextId = item.id + 1
            self.items.append(item)
        
    def to_dict(self):
        d = {
            'name': self.name,
            'items': []
        }
        for i in self.items:
            d['items'].append({
                'id': i.id,
                'name': i.name,
                'qty': i.qty
            })
        return d

    def add_item(self,item : Item, ref : object):
        #ref.update({"items":firestore.ArrayUnion([item.to_dict()])})
        ref.document(str(item.id)).set(item.to_dict())
        self.items.append(item)
    
    def remove_item(self,item : Item, ref : object):
        #ref.update({"items":firestore.ArrayRemove([item.to_dict()])})
        ref.document(str(item.id)).delete()
        self.items.remove(item)

    def update_item(self, item: Item, ref: object):
        id = item.id
        print(f"Current name: {item.name}")
        newName = input("Enter new name: ")
        if(newName != ""):
            item.name = newName
        print(f"Current quantity: {item.qty}")    
        newQty = input("Enter new quantity: ")
        if(newQty != ""):
            try:
                item.qty = int(newQty)
            except TypeError:
                print("Invalid quantity")
        ref.document(str(id)).update(item.to_dict())


    def get_item_id(self,id : int):
        for i in self.items:
            if i.id == id:
                return i
        return None
    
    def get_item_name(self,name : str):
        for i in self.items:
            if i.name == name:
                return i
        return None