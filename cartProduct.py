
class CartProduct:
    def addProduct(self,con,cur):

        print('------ Product Addition ------\n')
        
        username =  input('Enter username: ')
        cur.execute("SELECT * FROM cartuser where username='{}' and isAdmin=true".format(username))
        userList = cur.fetchall()
        if userList:
            categoryname =  input('Enter category name : ')
            cur.execute("SELECT id FROM category where categoryName='{}'".format(categoryname))
            category = cur.fetchone()
            if category:
                productName =  input('Enter product name : ')
                productDescription =  input('Enter product Description : ')
                productPrice =  float(input('Enter product Price : '))
                sql = "INSERT INTO product (categoryId,productName,productDescription,productPrice) \
                VALUES ('{}','{}','{}',{})".format(category[0],productName,productDescription,productPrice)
                cur.execute(sql)
                con.commit()
                print('------ Product Addition completed ------\n')
            else:
                print('------ This category is not present ------\n')

        else:
            print('------ Only Admins are allowed to perform this operation ------\n')


    def getAllProductsByCategory(self,con,cur):
        print('------ All Products ------\n')
        categoryname =  input('Enter category name : ')
        cur.execute("SELECT id FROM category where categoryName='{}'".format(categoryname))
        category = cur.fetchone()
        if category:
            cur.execute("SELECT * FROM product where categoryId={}".format(category[0]))
            productList = cur.fetchall()
            i = 0
            for product in productList:
                i += 1
                print(" ----- product ",i,"-----")
                print(" Product Id : ", product[1])
                print(" Product Name : ", product[2])
                print(" product Description : ", product[3])
                print(" Product Price : ",product[4])
                print("\n")
            print('------------\n')
        else:
            print('------ This category is not present ------\n')
        exit()