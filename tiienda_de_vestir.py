class product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def discount(self, discount):
        
        self.price -= discount 
         
#def print_products(self,**kwargs):   
def print_products(list):
        for product in list:
            if product.stock > 0:
                print(f"Name: {product.name}, Price: {product.price}, Stock: {product.stock}")   

shirt = product("shirt", 50, 20)
pants = product("pants", 70, 15)
shoes = product("shoes", 80, 10)
tie =   product("tie", 50, 10)
socks = product("socks", 20, 8)

""" for element in list_products  :
        if element.name == product_name:
            print(f"choice {element.name}")
            if element.stock >= quantity > 0 :
                print("great choice.")
                order = {"product_name": product_name, "quantity": quantity}
                order_list.append(order)
                break   
            elif quantity <= 0:
                print(f"quantity incorrect choose a quantity greater than zero")
                return 
            elif element.stock < quantity :
                print( f"quantity exceeds     only have {element.stock} {element.name} ")   
                            
    return order_list 


check_stock()
print(f"your order is {order_list}") 
                
 """
 
list_products = [
    shirt,
    pants,
    shoes,
    tie,
    socks,
]
print_products(list_products)

order_list = []
 
def check_stock():
    product_name = input("What product do you need?: ")
    try:
        quantity = int(input("Enter the quantity: "))
    except  ValueError: 
        print(f"ValueError write an integer ") 
        quantity = int(input("Enter the quantity: ")) 
    
    for element in list_products  :
        if element.name == product_name:
            print(f"choice {element.name}")
            if element.stock >= quantity > 0 :
                print("great choice.")
                order = {"product_name": product_name, "quantity": quantity}
                order_list.append(order)
                break
            elif quantity <= 0:
                print(f"quantity incorrect choose a quantity greater than zero")
                return 
            elif element.stock < quantity :
                print( f"quantity exceeds stock only have {element.stock} {element.name} ")  
                         
    return order_list 


check_stock()
print(f"your order is {order_list}") 
                
check_stock()
print(f"your order is {order_list}") 


