import unittest

class TestGiveMeOne(unittest.TestCase):

    def test_1(self):
        self.assertEqual(give_me_1(), 1)

    def test_wrong(self):
        self.assertEqual(give_me_1(), 2)

    def test_not_0(self):
        self.assertNotEqual(give_me_1(), 0)

    def test_int(self):
        self.assertEqual(type(give_me_1()), int)
