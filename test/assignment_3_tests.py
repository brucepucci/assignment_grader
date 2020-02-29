import unittest

class TestExercise1(unittest.TestCase):
    def test_1(self):
        self.assertIn(exercise_1([1, 2, 3, 4, 5, 6]), [[5, 6], [6, 5]])

    def test_2(self):
        self.assertEqual(exercise_1([1, 1, 1, 1, 1]), [1, 1])

    def test_3(self):
        self.assertIn(exercise_1([-100, -1000, -10000]), [[-1000, -100], [-100, -1000]])

    def test_4(self):
        self.assertEqual(exercise_1([0, 0]), [0, 0])

    def test_5(self):
        self.assertIn(exercise_1([1, 2, 1]), [[1, 2], [2, 1]])

    def test_6(self):
        self.assertIn(exercise_1([1.1, 2.1, 1.1]), [[1.1, 2.1], [2.1, 1.1]])


class TestExercise2(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_2(['a', 'b', 'c']), 0)

    def test_2(self):
        self.assertEqual(exercise_2(['Totally', 'Dude']), 1)

    def test_3(self):
        self.assertEqual(exercise_2(['Toronto', 'Torino', 'Toledo']), 3)

    def test_4(self):
        self.assertEqual(exercise_2(['Toronto']), 1)

    def test_5(self):
        self.assertEqual(exercise_2(['toronto', 'torino', 'toledo']), 0)


class TestExercise3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_3([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])

    def test_2(self):
        self.assertEqual(exercise_3([[1, 1, 1, 1, 1]]), [1, 1, 1, 1, 1])

    def test_3(self):
        self.assertEqual(exercise_3([[1], [2], [4], [6, 7]]), [1, 2, 4, 6, 7])

    def test_4(self):
        self.assertEqual(exercise_3([[1, 1, 1], [2], [4], [6, 7, 1]]), [1, 1, 1, 1, 2, 4, 6, 7])


class TestExercise4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len(exercise_4(['1', '1', '1', '1'])), 1)

    def test_2(self):
        self.assertEqual(exercise_4(['1', '1', '1', '1']), ['1'])

    def test_3(self):
        return_val = exercise_4(['Trump', 'Obama', 'Bush', 'Clinton', 'Bush'])
        self.assertEqual(len(return_val), 4)

    def test_4(self):
        return_val = exercise_4(['Trump', 'Obama', 'Bush', 'Clinton', 'Bush'])
        self.assertTrue(all(item in return_val for item in ['Clinton', 'Trump', 'Obama', 'Bush']))

    def test_5(self):
        return_val = exercise_4(['1', '2', '3', '4'])
        self.assertEqual(len(exercise_4(['1', '2', '3', '4'])), 4)

    def test_6(self):
        return_val = exercise_4(['1', '2', '3', '4'])
        self.assertTrue(all(item in return_val for item in ['1', '2', '3', '4']))


class TestExercise5(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_5([1, 2, 4, 5]), [1, 2, 'Hi!', 4, 5])

    def test_2(self):
        self.assertEqual(exercise_5([[], []]), [[], 'Hi!', []])

    def test_3(self):
        self.assertEqual(exercise_5(list('abcdef')), ['a', 'b', 'c', 'Hi!', 'd', 'e', 'f'])

    def test_4(self):
        self.assertEqual(exercise_5([1, 2, 4, 5, 7, 8]), [1, 2, 4, 'Hi!', 5, 7, 8])

    def test_5(self):
        self.assertEqual(exercise_5([1, 1]), [1, 'Hi!', 1])


class TestExercise6(unittest.TestCase):
    def test_1(self):
        self.assertTrue(exercise_6(['a', 'b', 'a']))

    def test_2(self):
        self.assertFalse(exercise_6(['a', 'b' 'c']))

    def test_3(self):
        self.assertTrue(exercise_6(['-1']))

    def test_4(self):
        self.assertTrue(exercise_6(['a', 'b', 'a', 'a']))

    def test_5(self):
        self.assertFalse(exercise_6(['a', 'b' 'c', 'a', 'd']))

    def test_6(self):
        self.assertTrue(exercise_6(['-1', '-1']))


class TestExercise7(unittest.TestCase):
    def test_1(self):
        self.assertIn(exercise_7([1, 2, 3, 4, 5, 6]), [[4, 5], [5, 4]])

    def test_2(self):
        self.assertIn(exercise_7([-100, -1000, -10000]), [[0, 1], [1, 0]])

    def test_3(self):
        self.assertIn(exercise_7([1, 1]), [[0, 1], [1, 0]])

    def test_4(self):
        self.assertIn(exercise_7([1, 1, 1]), [[0, 1], [1, 0], [0, 2], [2, 0], [1, 2], [2, 1]])
