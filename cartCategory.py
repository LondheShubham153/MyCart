
class CartCategory:
    
    def __init__(self, con, cur,username):
        self.con = con
        self.cur = cur
        self.username = username

    def addCategory(self):

        print('------ Category Addition ------\n')
        
        self.cur.execute("SELECT * FROM cartuser where username='{}' and isAdmin=true".format(self.username))
        userList = self.cur.fetchall()
        if userList:
            categoryname =  input('Enter category name : ')
            sql = "INSERT INTO category (categoryName) VALUES ('{}')".format(categoryname)
            self.cur.execute(sql)
            self.con.commit()
            print('------ Category Addition completed ------\n')
        else:
            print('------ Only Admins are allowed to perform this operation ------\n')


    def getAllCategories(self):
        print('------ All categories ------\n')
        self.cur.execute("SELECT * FROM category")
        categoryList = self.cur.fetchall()
        i = 0
        for category in categoryList:
            i += 1
            print(" ----- category ",i,"-----")
            print(" Category name : ", category[1])
            print(" Date Created : ", category[2])
            print("\n")
        print('------------\n')