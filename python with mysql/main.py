


# import mysql.connector as connector
# con = connector.connect(host='localhost',
#                         port='3306',
#                         user='root',
#                         password='Rewa1234',
#                         database = 'pythontest')

# print(con)

             # lesson 2

import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='Rewa1234',
                                     database='pythontest')
        query = 'create table if not exists user(userid int primary key,userName varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

# main coding
helper = DBHelper()


          # lesson 3

import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='Rewa1234',
                                     database='pythontest')
        query = 'create table if not exists user(userid int primary key,userName varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")


        # insert
    
    def insert_user(self, userid , username,phone):
        query= "insert into user(userid, userName ,phone) value({},'{}','{}')".format(userid,username,phone)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

# main coding
helper = DBHelper()
#helper.insert_user(1568, "ashwani", "4579890")

helper.insert_user(15645, "nitesg", "45774")
helper.insert_user(15788, "pyushr", "457457")


                    # lesson 4


# import mysql.connector as connector

# class DBHelper:
#     def __init__(self):
#         self.con = connector.connect(host='localhost',
#                                      port='3306',
#                                      user='root',
#                                      password='Rewa1234',
#                                      database='pythontest')
#         query = 'create table if not exists user(userid int primary key,userName varchar(200),phone varchar(12))'
#         cur = self.con.cursor()
#         cur.execute(query)
#         print("created")


#         # insert
    
#     def insert_user(self, userid , username,phone):
#         query= "insert into user(userid, userName ,phone) value({},'{}','{}')".format(userid,username,phone)
#         print(query)
#         cur=self.con.cursor()
#         cur.execute(query)
#         self.con.commit()
#         print("user saved to db")
    

#     # Fech all
#     def fetch_all(self):
#         query="select * from user"
#         cur=self.con.cursor()
#         cur. execute(query)
#         for row in cur:
#             print(row)

# # main coding
# helper = DBHelper()

# helper.fetch_all()



# lesson 5



# import mysql.connector as connector

# class DBHelper:
#     def __init__(self):
#         self.con = connector.connect(host='localhost',
#                                      port='3306',
#                                      user='root',
#                                      password='Rewa1234',
#                                      database='pythontest')
#         query = 'create table if not exists user(userid int primary key,userName varchar(200),phone varchar(12))'
#         cur = self.con.cursor()
#         cur.execute(query)
#         print("created")


#         # insert
    
#     def insert_user(self, userid , username,phone):
#         query= "insert into user(userid, userName ,phone) value({},'{}','{}')".format(userid,username,phone)
#         print(query)
#         cur=self.con.cursor()
#         cur.execute(query)
#         self.con.commit()
#         print("user saved to db")
    

#     # Fech all
#     def fetch_all(self):
#         query="select * from user"
#         cur=self.con.cursor()
#         cur. execute(query)
#         for row in cur:
#             print(row)



#               # delete user


#     def delete_user(self,userid):
#         query = "delete from user where userid= {}" . format(userid)
#         print(query)
#         c=self.con.cursor()
#         c.execute(query)
#         self.con .commit()
#         print("deleted")        

# # main coding
# helper = DBHelper()

# #helper.fetch_all()
# helper.delete_user(1452)
# helper.fetch_all()



#        # lesson 6

# import mysql.connector as connector

# class DBHelper:
#     def __init__(self):
#         self.con = connector.connect(host='localhost',
#                                      port='3306',
#                                      user='root',
#                                      password='Rewa1234',
#                                      database='pythontest')
#         query = 'create table if not exists user(userid int primary key,userName varchar(200),phone varchar(12))'
#         cur = self.con.cursor()
#         cur.execute(query)
#         print("created")


#         # insert
    
#     def insert_user(self, userid , username,phone):
#         query= "insert into user(userid, userName ,phone) value({},'{}','{}')".format(userid,username,phone)
#         print(query)
#         cur=self.con.cursor()
#         cur.execute(query)
#         self.con.commit()
#         print("user saved to db")
    

#     # Fech all
#     def fetch_all(self):
#         query="select * from user"
#         cur=self.con.cursor()
#         cur. execute(query)
#         for row in cur:
#             print(row)



#               # delete user


#     def delete_user(self,userid):
#         query = "delete from user where userid= {}" . format(userid)
#         print(query)
#         c=self.con.cursor()
#         c.execute(query)
#         self.con .commit()
#         print("deleted")  


#         # update user

#     def update_user(self,userid,newName,newphone):
#         query="update user set userName='{}',phone='{}' where userid={}".format(newName,newphone,userid)
#         print(query)
#         cur=self.con.cursor()
#         cur.execute(query)
#         self.con.commit()
#         print("updated")


# # main coding
# helper = DBHelper()

# #helper.fetch_all()
# #helper.delete_user(1452)
# #helper.fetch_all()
# helper.update_user(15645, 'pyush raj', '123456789')






# from dbhelper import DBHelper

# def main():
#     db=DBHelper()


#     while True:
#         print("***********WELCOME************")
#         print()
#         print("PRESS 1 to insert new user")
#         print("PRESS 2 to  display all user")
#         print("PRESS 3 to delete user")
#         print("PRESS 4 to update user ")
#         print("PRESS 5 to exit program")
#         print()
#         try:
#             choice = int(input())
#             if(choice==1):
#                 # insert user
#                 uid = int(input("Enter user id"))
#                 username = input("Enter user name")
#                 userphone = input("Enter user phone")
#                 db.insert_user(uid, username, userphone)

                
#             elif choice==2:

#                 # display user
#                 db.fetch_all()
#                 pass   

                
#             elif choice==3:
#                 #delete user
#                 userid = int(input('enter user id to which you want to delete'))
#                 db.delete_user(userid)
#                 pass
#             elif choice==4:
#                 #update user
#                 uid = int(input("enter id of user "))
#                 username = input("new name ")
#                 userphone = input("new phone")
#                 db.update_user(uid, username, userphone)
#                 pass
#             elif choice==5:
#                 break
#             else:
#                 print("invalid input  ! try again")
#         except Exception as e:
#             print(e)
#             print("invalid details  ! try again")

# if __name__ == "__main__":
#     main()
