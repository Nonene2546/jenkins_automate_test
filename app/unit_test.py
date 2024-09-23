import unittest
from werkzeug import exceptions

import app

class AppTestCase(unittest.TestCase):
    def test_happy_plus(self):
        res = app.plus(1, 4).response.pop()
        self.assertEqual(res, b'3\n')
    
    def test_first_num_invalid(self):
        with self.assertRaises(exceptions.BadRequest):
            app.plus(1, "2+9/5")
    
    def test_second_num_invalid(self):
        with self.assertRaises(exceptions.BadRequest):
            app.plus("2+9/5", 5)
    
    def test_both_num_invalid(self):
        with self.assertRaises(exceptions.BadRequest):
            app.plus("2+9/5", "2+9/5")

if __name__ == "__main__":
    with app.app.app_context():
        unittest.main()