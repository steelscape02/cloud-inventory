from typing import List
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
    def from_dict(self,d : dict):
        self.name = d['name']
        self.items = [] #empty init
        for i in d['items']:
            item = Item(i['name'],i['qty'])
            item.id = i['id']
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

    def add_item(self,item : Item):
        self.items.append(item)
    
    def remove_item(self,item : Item):
        self.items.remove(item)

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