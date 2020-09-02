import pymysql.connections
class Mydb:
    def __init__(self):
        self.my_connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='Airline Ticket Booking System')

        self.cursor = self.my_connection.cursor()
