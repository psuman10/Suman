from Backend.Connection import Mydb

class Airline(Mydb):
    def __init__(self):

        super().__init__()

    def login(self, username, password):
        try:
            qry = "select * from registration where username=%s and password=%s"
            values = (username, password)
            self.cursor.execute(qry, values)
            data = self.cursor.fetchone()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)

    def signup(self, username, password, FullName, Address, Country, Email, PassportNo):
        try:
            qry = "INSERT INTO registration (username,password,name,address,phone,email,passport)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (username, password, FullName, Address, Country, Email, PassportNo)
            self.cursor.execute(qry, values)


            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)


    def add(self, passport, name, gender, date, pickup, email, boarding):
        try:
            qry = "INSERT INTO booking " \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (passport, name, gender, date, pickup, email, boarding)
            self.cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)

    def update(self,name, gender, date, pickup, email,passport,boarding):
        try:
            qry = "Update booking set name=%s,gender=%s,date=%s,pickup=%s,email=%s,boarding=%s where passport=%s"
            values = (name, gender, date, pickup, email,boarding,passport)
            self.cursor.execute(qry, values)
            self.my_connection.commit()
            return True
        except Exception as e:
            print(e)

    def fetch_data(self):
        try:
            qry = 'select * from booking order by name'
            self.cursor.execute(qry)
            data = self.cursor.fetchall()
            self.my_connection.close()
            return data
        except Exception as e:
            print(e)
#
    def delete_datas(self, passport):
        try:
            qry = 'delete from booking where passport=%s'
            values = (passport,)
            self.cursor.execute(qry, values)
            self.my_connection.commit()
            self.my_connection.close()
            return True
        except Exception as e:
            print(e)
#
    def search_data(self, search_by, search):
        try:
            qry = ("select * from booking where " + search_by + "  like '" + search + "%' ")
            self.cursor.execute(qry)
            self.my_connection.close()
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            print(e)

s=Airline
