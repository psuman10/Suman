import unittest
from Backend.air_query import Airline

class MyTest(unittest.TestCase):
    def test_add(self):
        a = Airline()
        actual_result = a.add('49502', 'suman parajuli', 'Male', '12/20/2021', 'sydney', 'Sp554540@gmail.com', 'Kathmandu-Nepal')
        self.assertTrue(actual_result)

    def test_update(self):
        b = Airline()
        actual_result = b.update('190265', 'suman parajuli', 'Male', '12/20/2021', 'brisbane', 'Sp554540@gmail.com', 'Kathmandu-Nepal')
        self.assertTrue(actual_result)

    def test_fetch_data(self):
        c = Airline()
        actual_result = c.fetch_data()
        self.assertTrue(actual_result)

    def test_login(self):
        d = Airline()
        actual_result = d.login('1', '1')
        self.assertTrue(len(actual_result), 1)

    def test_signup(self):
        e = Airline()
        actual_result = e.signup('190265','sp', '49501', 'suman parajuli', 'ktm', 'nepal', 'psuman9840@gmail.com')
        self.assertTrue(actual_result)

    def test_delete_datas(self):
        e = Airline()
        actual_result = e.delete_datas('passport')
        self.assertTrue(actual_result)


