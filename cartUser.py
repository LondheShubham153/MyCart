
class CartUser:
    def registerUser(self,con,cur,isAdmin=None):

        print('------ User Registration ------\n')
        
        username =  input('Enter username : ')
        email =  input('Enter email : ')
        if isAdmin:
            sql = 'INSERT INTO cartuser (username,email,isAdmin) VALUES (%s,%s,%s)'
            val = (username,email,isAdmin)
        else:    
            sql = 'INSERT INTO cartuser (username,email) VALUES (%s,%s)'
            val = (username,email)
        cur.execute(sql,val)
        con.commit()
        print('------ USER REGISTRATION COMPLETED ------\n')


    def getAllUsers(self,con,cur):
        print('------ All Users ------\n')
        cur.execute("SELECT * FROM cartuser")
        userList = cur.fetchall()
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
        exit()