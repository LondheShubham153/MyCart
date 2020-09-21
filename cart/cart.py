import json
import time
import pprint

class Cart:
    
    def __init__(self, con, cur,username):
        self.items_in_cart = {}
        self.amount = 0
        self.con = con
        self.cur = cur
        self.username = username
        self.discount = 500

    def addProductToCart(self):
        
        print('------ Product Addition To cart------\n')
        
        while True:
            productId =  input('Enter product id : ')
            self.cur.execute("SELECT * FROM product where productId={}".format(productId))
            product = self.cur.fetchone()
            if product:
                if not product[2] in self.items_in_cart:
                    self.items_in_cart[product[2]] = str(product[4])
                    self.amount += product[4] 
                    pprint.pprint(self.items_in_cart)

                    print("Cart Total: "+ str(self.amount)+"\n")
                else:
                    print("Product is already in the cart.")

                choice = input('1) Add Another product to cart\n2) Remove Product from Cart\n3) Proceed to Checkout?\n ')
                if choice == "2":
                    self.removeProductfromCart()
                    break
                elif choice == "3":
                    self.generateBill()
                    break

    def removeProductfromCart(self):
        
        print('------ Product Removal From cart------\n')
        
        while True:
            productId =  input('Enter product id : ')
            self.cur.execute("SELECT * FROM product where productId={}".format(productId))
            product = self.cur.fetchone()
            if product:
                if product[2] in self.items_in_cart:
                    self.items_in_cart.pop(product[2])
                    self.amount -= product[4] 
                    pprint.pprint(self.items_in_cart)

                    print("Cart Total: "+ str(self.amount)+"\n")
                else:
                    print("Product is not present in the cart.")

                choice = input('1) Add Another product to cart\n2) Remove Product from Cart\n3) Proceed to Checkout? ')
                if choice == "1":
                    self.addProductToCart()
                    break
                elif choice == "3":
                    self.generateBill()
                    break

    def generateBill(self):
        
        print('------ Generating Bill ------\n')
        time.sleep(1)
        
        self.cur.execute("SELECT * FROM cartuser where username='{}'".format(self.username))
        user = self.cur.fetchone()
        for item,price in self.items_in_cart.items():
            print("Item: "+item +" Price: "+price)
        
        print("Total: "+str(self.amount))

        bill = json.dumps(self.items_in_cart)
        if self.amount > 10000:
            self.amount = self.amount-self.discount
            print("Amount after Discount: "+ str(self.amount))
        
        sql = "INSERT INTO bill (userId,bill,amount) \
                VALUES ('{}','{}',{})".format(user[0],bill,self.amount)
        
        self.cur.execute(sql)
        self.con.commit()
                
    def getBillForUser(self):
        username =  input('Enter username : ')
        self.cur.execute("SELECT id FROM cartuser where username='{}'".format(username))
        user = self.cur.fetchone()
        self.cur.execute("SELECT * FROM bill where userId={}".format(user[0]))
        bills = self.cur.fetchall()
        i = 0
        for bill in bills:
            i += 1
            print(" ----- Bill ",i,"-----")
            print(" Bill Id : ", bill[0])
            print(" Bill : ", json.loads(bill[2]))
            print(" Amount : ", bill[3])
            print(" Bill Dated : ", bill[4])
            print("\n")
        print('------------\n')

        time.sleep(1)

        
        
