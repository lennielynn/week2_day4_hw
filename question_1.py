

class ShoppingList:
    pass

    def __init__(self, items, remove):
        self.items = items
        self.remove = remove
        
    def displayList(self):
        print(self.items)
        
    def addItems(self):
        l_item = input("Enter Item: ")
        self.items.append(l_item)
    
    def itemRemove(self):
        print(self.items)
        item_del = input("What would you like removed? ")
        self.items.remove(item_del)
    
def driver():
        while True:
          response = input('Add, Remove, View, or Quit? ')
        
          if response.lower() == 'quit':
            bag.displayList()
            print('Thanks for shopping!')
            break
          elif response.lower() == 'add':
            bag.addItems()
          elif response.lower() == 'remove':
            bag.itemRemove()
          elif response.lower() == 'view':
            bag.displayList()
            
bag = ShoppingList([],[])

driver()