import unittest

class TestExercise1(unittest.TestCase):
    def test_1(self):
        return_val = exercise_1(['a', 'b', 'c', 'a', 'a'])
        self.assertEqual(return_val['a'], 3)

    def test_2(self):
        return_val = exercise_1(['a', 'b', 'c', 'a', 'a'])
        self.assertEqual(return_val['b'], 1)

    def test_3(self):
        return_val = exercise_1(['a', 'b', 'c', 'a', 'a'])
        self.assertEqual(return_val['c'], 1)

    def test_4(self):
        return_val = exercise_1(['a'])
        self.assertEqual(return_val['a'], 1)

    def test_5(self):
        return_val = exercise_1(['a', 'b', 'c', 'a', 'a', 'a', 'b'])
        self.assertEqual(len(return_val.keys()), 3)

    def test_6(self):
            return_val = exercise_1(['a', 'b', 'c', 'a', 'a', 'a', 'b'])
            self.assertEqual(sum(return_val.values()), 7)


class TestExercise2(unittest.TestCase):
    def test_1(self):
        self.assertTrue(exercise_2('a'))

    def test_2(self):
        self.assertFalse(exercise_2('b'))

    def test_3(self):
        self.assertFalse(exercise_2('A'))

    def test_4(self):
        self.assertFalse(exercise_2('B'))

    def test_5(self):
        self.assertTrue(exercise_2(6))


class TestExercise3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_3({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_2(self):
        self.assertEqual(exercise_3({'a': -100, 'b': 0, 'c': 100}), 0)

    def test_3(self):
        self.assertEqual(exercise_3({'b': 0,}), 0)


class TestExercise4(unittest.TestCase):
    def test_1(self):
        return_val = exercise_4({'a': 4, 'world': 'hello', 'my_list': []})
        self.assertEqual(return_val['a'], 4)

    def test_2(self):
        return_val = exercise_4({'a': 4, 'world': 'hello', 'my_list': []})
        self.assertEqual(return_val['hello'], 'world')

    def test_3(self):
        return_val = exercise_4({'a': 4, 'world': 'hello', 'my_list': []})
        self.assertEqual(return_val['world'], 'hello')

    def test_4(self):
        return_val = exercise_4({'a': 4, 'world': 'hello', 'my_list': []})
        self.assertEqual(return_val['my_list'], [])

    def test_5(self):
        return_val = exercise_4({'a': 4, 'world': 'hello', 'my_list': []})
        self.assertEqual(len(return_val.keys()), 6)

    def test_6(self):
        return_val = exercise_4({'a': 4, 'world': 'hello', 'my_list': []})
        self.assertEqual(return_val['Case'], 'Western Reserve')


class TestExercise5(unittest.TestCase):
    def test_1(self):
        self.assertEqual(exercise_5({'a': 4, 'b': 10, 'c': 100, 'd': -100, 'e': 50}), 'c')

    def test_2(self):
        self.assertEqual(exercise_5({'a': -1, 'b': -2, 'c': -6, 'd': -100, 'e': -1000}), 'a')

    def test_3(self):
        self.assertEqual(exercise_5({'a': -1}), 'a')

    def test_5(self):
        self.assertEqual(exercise_5({'b': -2, 'c': -6, 'z': -1, 'd': -100, 'e': -1000}), 'z')


class TestExercise6(unittest.TestCase):
    def test_1(self):
        return_val = exercise_6([['a', 'b', 'c'], [1, 2, 3]])
        self.assertEqual(return_val['a'], 1)

    def test_2(self):
        return_val = exercise_6([['a', 'b', 'c'], [1, 2, 3]])
        self.assertEqual(return_val['b'], 2)

    def test_3(self):
        return_val = exercise_6([['a', 'b', 'c'], [1, 2, 3]])
        self.assertEqual(return_val['c'], 3)

    def test_4(self):
        return_val = exercise_6([['a', 'b', 'c'], [1, 2, 3]])
        self.assertEqual(len(return_val.keys()), 3)

    def test_5(self):
        return_val = exercise_6([[1, 2, 3, 4], ['a', 'b', 'c', 'd']])
        self.assertEqual(return_val[1], 'a')

    def test_6(self):
        return_val = exercise_6([[1, 2, 3, 4], ['a', 'b', 'c', 'd']])
        self.assertEqual(return_val[2], 'b')

    def test_7(self):
        return_val = exercise_6([[1, 2, 3, 4], ['a', 'b', 'c', 'd']])
        self.assertEqual(return_val[3], 'c')

    def test_8(self):
        return_val = exercise_6([[1, 2, 3, 4], ['a', 'b', 'c', 'd']])
        self.assertEqual(return_val[4], 'd')

    def test_9(self):
        return_val = exercise_6([[1, 2, 3, 4], ['a', 'b', 'c', 'd']])
        self.assertEqual(len(return_val.keys()), 4)

    def test_10(self):
        return_val = exercise_6([[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']])
        self.assertEqual(return_val[5], 'e')