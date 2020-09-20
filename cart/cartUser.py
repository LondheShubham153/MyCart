
class CartUser:

    def __init__(self, con, cur):
        self.con = con
        self.cur = cur

    def registerUser(self,isAdmin=None):

        print('------ User Registration ------\n')
        
        username =  input('Enter username : ')
        email =  input('Enter email : ')
        if isAdmin:
            sql = 'INSERT INTO cartuser (username,email,isAdmin) VALUES (%s,%s,%s)'
            val = (username,email,isAdmin)
        else:    
            sql = 'INSERT INTO cartuser (username,email) VALUES (%s,%s)'
            val = (username,email)
        self.cur.execute(sql,val)
        self.con.commit()
        print('------ USER REGISTRATION COMPLETED ------\n')


    def getUser(self,email):
        self.cur.execute("SELECT * FROM cartuser where email='{}'".format(email))
        username = self.cur.fetchone()
        if username:
            return username[1]
        else:
            return None

    def getAllUsers(self):
        print('------ All Users ------\n')
        self.cur.execute("SELECT * FROM cartuser")
        userList = self.cur.fetchall()
        i = 0
        for user in userList:
            i += 1
            print(" ----- User ",i,"-----")
            print(" Username : ", user[1])
            print(" Date Joined : ", user[2])
            print(" Email : ", user[3])
            print(" Admin Access : ", user[4])
            print("\n")
        print('------------\n')