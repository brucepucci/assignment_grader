import unittest

class TestExercise1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_1(5), 5)

    def test_2(self):
        self.assertNotEqual(exercise_1(10), 4)

    def test_3(self):
        self.assertNotEqual(exercise_1(100), 6)

    def test_4(self):
        self.assertEqual(exercise_1(5), 5.0)

    def test_5(self):
        self.assertEqual(exercise_1(0), 5)

    def test_6(self):
        self.assertEqual(exercise_1(5), 5)

    def test_7(self):
        self.assertIs(type(exercise_1(5)), int)


class TestExercise2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_2('Ahhh'), 'Ahhh!!!')

    def test_2(self):
        self.assertEqual(exercise_2(' '), ' !!!')

    def test_3(self):
        self.assertEqual(exercise_2("""

whoa"""), '\n\nwhoa!!!')

    def test_4(self):
        self.assertEqual(exercise_2(''), '!!!')

    def test_5(self):
        self.assertEqual(exercise_2('!!!'), '!!!!!!')


class TestExercise3(unittest.TestCase):
    def test_1(self):
        self.assertFalse(exercise_3('abc'))

    def test_2(self):
        self.assertTrue(exercise_3('England'))

    def test_3(self):
        self.assertTrue(exercise_3(''))

    def test_4(self):
        self.assertFalse(exercise_3('        '))


class TestExercise4(unittest.TestCase):
    def test_1(self):
        self.assertTrue(exercise_4(1.0))

    def test_2(self):
        self.assertFalse(exercise_4(-900))

    def test_3(self):
        self.assertFalse(exercise_4(-80))

    def test_4(self):
        self.assertFalse(exercise_4(-80.1))

    def test_5(self):
        self.assertTrue(exercise_4(20))

    def test_6(self):
        self.assertTrue(exercise_4(-79.9))


class TestExercise5(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_5(-100), 100)

    def test_2(self):
        self.assertEqual(exercise_5(100.1), 100.1)

    def test_3(self):
        self.assertEqual(exercise_5(100), 100)

    def test_4(self):
        self.assertEqual(exercise_5(0), 100)


class TestExercise6(unittest.TestCase):
    def test_1(self):
        self.assertFalse(exercise_6(' '))

    def test_2(self):
        self.assertFalse(exercise_6('abcdefg'))

    def test_3(self):
        self.assertTrue(exercise_6('ab'))

    def test_4(self):
        self.assertTrue(exercise_6('abab'))


class TestExercise7(unittest.TestCase):
    def test_1(self):
        self.assertFalse(exercise_7(3))

    def test_2(self):
        self.assertFalse(exercise_7(4))

    def test_3(self):
        self.assertTrue(exercise_7(15))

    def test_4(self):
        self.assertTrue(exercise_7(30))

    def test_5(self):
        self.assertTrue(exercise_7(15000))

    def test_6(self):
        self.assertFalse(exercise_7(1))


class TestExercise8(unittest.TestCase):
    def test_1(self):
        self.assertFalse(exercise_8(8))

    def test_2(self):
        self.assertTrue(exercise_8(10))

    def test_3(self):
        self.assertFalse(exercise_8(6))

    def test_4(self):
        self.assertTrue(exercise_8(16))

    def test_5(self):
        self.assertTrue(exercise_8(18))

    def test_6(self):
        self.assertFalse(exercise_8(1))


class TestExercise9(unittest.TestCase):
    def test_1(self):
        self.assertIn('"', exercise_9())

    def test_2(self):
        self.assertIn('"', exercise_9())

    def test_3(self):
        self.assertIs(type(exercise_9()), str)


class TestExercise10(unittest.TestCase):
    def test_1(self):
        self.assertTrue(exercise_10(0))

    def test_2(self):
        self.assertFalse(exercise_10('0'))

    def test_3(self):
        self.assertTrue(exercise_10(0.0))

    def test_4(self):
        self.assertFalse(exercise_10(None))
