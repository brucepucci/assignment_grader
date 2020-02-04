import unittest

class TestExercise1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_1(1), 2)

    def test_2(self):
        self.assertEqual(exercise_1(4.), 16.)

    def test_3(self):
        self.assertEqual(exercise_1(100), 200)

    def test_4(self):
        self.assertEqual(exercise_1(100.), 10000.)

    def test_5(self):
        self.assertEqual(exercise_1(0.), 0.)

    def test_6(self):
        self.assertEqual(exercise_1(0), 0)

    def test_7(self):
        self.assertEqual(exercise_1(-1.2), 1.44)

    def test_8(self):
        self.assertEqual(exercise_1(-100), -200)


class TestExercise2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_2(0), 'F')

    def test_2(self):
        self.assertEqual(exercise_2(70), 'C')

    def test_3(self):
        self.assertEqual(exercise_2(80.00001), 'B')

    def test_4(self):
        self.assertEqual(exercise_2(80), 'B')

    def test_5(self):
        self.assertEqual(exercise_2(100), 'A')

    def test_6(self):
        self.assertEqual(exercise_2(90), 'A')

    def test_7(self):
        self.assertEqual(exercise_2(60), 'D')

    def test_8(self):
        self.assertEqual(exercise_2(100), 'A')


class TestExercise3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_3(2020), 'Leap Year')

    def test_2(self):
        self.assertEqual(exercise_3(2010), 'Not Leap Year')

    def test_3(self):
        self.assertEqual(exercise_3(0), 'Leap Year')

    def test_4(self):
        self.assertEqual(exercise_3(2019), 'Not Leap Year')

    def test_5(self):
        self.assertEqual(exercise_3(2021), 'Not Leap Year')

    def test_6(self):
        self.assertEqual(exercise_3(4000000), 'Leap Year')

    def test_7(self):
        self.assertEqual(exercise_3(-4000000), 'Leap Year')


class TestExercise4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_4(2), 10)

    def test_2(self):
        self.assertEqual(exercise_4(6), 286)

    def test_3(self):
        self.assertEqual(exercise_4(1), 1)

    def test_4(self):
        self.assertEqual(exercise_4(3), 35)

    def test_5(self):
        self.assertEqual(exercise_4(70), 457310)


class TestExercise5(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_5(8), 128)

    def test_2(self):
        self.assertEqual(exercise_5(100), 20000)

    def test_3(self):
        self.assertEqual(exercise_5(2), 8)

    def test_4(self):
        self.assertEqual(exercise_5(12), 288)

    def test_5(self):
        self.assertEqual(exercise_5(5000), 50000000)


class TestExercise6(unittest.TestCase):
    def test_1(self):
        self.assertIn(exercise_6(2), ['hello_hello', 'hello-hello'])

    def test_2(self):
        self.assertIn(exercise_6(5), ['hello-hello_hello-hello_hello',
                                      'hello_hello-hello_hello-hello'])

    def test_3(self):
        self.assertIn(exercise_6(1), 'hello')

    def test_4(self):
        self.assertIn(exercise_6(3), ['hello-hello_hello',
                                      'hello_hello-hello'])

    def test_5(self):
        self.assertIn(exercise_6(6), ['hello-hello_hello-hello_hello-hello',
                                      'hello_hello-hello_hello-hello_hello'])
