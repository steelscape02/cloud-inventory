class Item:
    nextId = 0
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty
        self.id = Item.nextId
        Item.nextId += 1

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'qty': self.qty
        }
    
    def __str__(self):
        return f'{self.id} - {self.name}: {self.qty}'