from typing import List
from Item import Item

class Inventory:
    def __init__(self,name : str,items : List[Item]):
        self.name = name
        self.items = items

    def __str__(self):
        for i in self.items:
            print(i)
    
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