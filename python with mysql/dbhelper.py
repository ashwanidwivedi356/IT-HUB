




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
    

    # Fech all
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur. execute(query)
        for row in cur:
            print(row)



              # delete user


    def delete_user(self,userid):
        query = "delete from user where userid= {}" . format(userid)
        print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con .commit()
        print("deleted")  


        # update user

    def update_user(self,userid,newName,newphone):
        query="update user set userName='{}',phone='{}' where userid={}".format(newName,newphone,userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")


# main coding
helper = DBHelper()

helper.fetch_all()
#helper.delete_user(1452)
#helper.fetch_all()
#helper.insert_user(1568, "ashwani", "4579890")

#helper.insert_user(15788, "pyushr", "457457")

helper.update_user(15645, 'pyush raj', '123456789')



