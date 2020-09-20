
class CartCategory:
    def addCategory(self,con,cur):

        print('------ Category Addition ------\n')
        
        username =  input('Enter username: ')
        cur.execute("SELECT * FROM cartuser where username='{}' and isAdmin=true".format(username))
        userList = cur.fetchall()
        if userList:
            categoryname =  input('Enter category name : ')
            sql = "INSERT INTO category (categoryName) VALUES ('{}')".format(categoryname)
            cur.execute(sql)
            con.commit()
            print('------ Category Addition completed ------\n')
        else:
            print('------ Only Admins are allowed to perform this operation ------\n')


    def getAllCategories(self,con,cur):
        print('------ All categories ------\n')
        cur.execute("SELECT * FROM category")
        categoryList = cur.fetchall()
        i = 0
        for category in categoryList:
            i += 1
            print(" ----- category ",i,"-----")
            print(" Category name : ", category[1])
            print(" Date Created : ", category[2])
            print("\n")
        print('------------\n')
        exit()