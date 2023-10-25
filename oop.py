class Item:
    pay_rate =0.8
    all=[]
    def __init__(self, name: str , price: int , quantity=0):
        
        #Run validation with assert

        assert price >=0 , f"price {price} is not greater or equal to zero"
        assert quantity >=0 ,f"quantity {quantity} is not greater or equal to zero"

        #Assigning self object 
        self.name=name
        self.price=price
        self.quantity= quantity
        
        #Action to execute
        Item.all.append(self)

    def calculate_two_numbers(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price =self.price * self.pay_rate
    
    def __repr__(self):
        return f'Item({self.name},{self.price},{self.quantity})'


item1 = Item("phone", 1000, 4)
item2 = Item("laptop" , 400, 3)
item3 = Item("mouse" , 200, 5)
item4 = Item("keyboard" , 100, 8)
item5 = Item("camera" , 440, 7)


#print(Item.all)


#inheritance of Item 

class Phone(Item):
    all=[]
    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
            )

        self.broken_phones =broken_phones

        Phone.all.append(self)

phone =Phone("techno", 34, 10)
phone.broken_phones=1

print(phone.broken_phones)
    