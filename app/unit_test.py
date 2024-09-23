import unittest
from werkzeug import exceptions

import app
from app import app as flask_instance

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app_context = flask_instance.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_happy_plus(self):
        res = app.plus(1, 4)
        self.assertEqual(res.get_json(), 5)
    
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
    unittest.main()