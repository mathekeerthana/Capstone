# sample code

class Product_a:
    def __init__(self,Name,price,Dealprice,Rating):
        self.Name=Name
        self.price=price
        self.Dealprice=Dealprice
        self.Rating=Rating
    def display_product(self):
        print("Name:",self.Name)
        print("price:",self.price)
        print("Dealprice:{}".format(self.Dealprice))
        print("Rating:{}".format(self.Rating))
    def get_Dealprice(self):
        return self.Dealprice


class Electronic_products(Product_a):

    def Set_waranty(self,waranty):
         self.waranty=waranty

    def Get_waranty(self):
        return self.waranty

class Grossary_products(Product_a):

    def __init__(self,Name,price,Dealprice,Rating,Packing_date,Expiry_date):
        super().__init__(Name,price,Dealprice,Rating)
        self.Packing_date=Packing_date
        self.Expiry_date = Expiry_date

    def display_product(self):
        super().display_product()
        print("Packing date:{}".format(self.Packing_date))

        print("Expiry date:{}".format(self.Expiry_date))


class Order:
    def __init__(self, delivery_Type, delivery_Address):
        self.items = []  # Empty List
        self.delivery_Type = delivery_Type
        self.delivery_Address = delivery_Address

    def add_items(self, product, quantity):
        self.items.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items:
            product.dispaly_product()
            print("Quantity:{}".format(quantity))

    def display_total_bill(self):
        total_bill=0
        for product,quantity in self.items:
            price=product.get_Dealprice() * quantity
            total_bill +=price
        print("Total Bill:{}".format(total_bill))


milk=Grossary_products("Milk",30,20,9)

tv=Electronic_products("TV",40000,35000,5)

order=Order("prime Delivary","Hyderabad")

order.add_items(milk,2)









productobj=Product_a("Milk",20,2,4)
productobj.display_product()

print("==========================")

electronicobj=Electronic_products("vivo 1935",10,8,5)
electronicobj.display_product()

print("==========================")

grossaryobj=Grossary_products("oil",30,20,5,2022,2023)
grossaryobj.display_product()

class Order:
    def __init__(self,delivery_Type,delivery_Address):
        self.items=[]         # Empty List
        self.delivery_Type=delivery_Type
        self.delivery_Address=delivery_Address

    def add_items(self,product,quantity):
        self.items.append((product,quantity))

    def display_order_details(self):
        for product,qyantity in self.items:
            price=product.



