import unittest

class TestExercise1(unittest.TestCase):
    def test_1(self):
        assert is_palindrome('12345') == False

    def test_2(self):
        assert is_palindrome('12321') == True
    
    def test_3(self):
        assert is_palindrome('123321') == True


class TestExercise2(unittest.TestCase):
    def test_1(self):
        assert swap_case('TESTING') == 'testing'

    def test_2(self):
        assert swap_case('Testing') == 'tESTING'
    
    def test_3(self):
        assert swap_case('testing') == 'TESTING'


class TestExercise3(unittest.TestCase):
    def test_1(self):
        result = count_lead_letter('this is totally a testy test')
        assert result['t'] == 4

    def test_2(self):
        result = count_lead_letter('this is totally a testy test')
        assert result['a'] == 1
    
    def test_3(self):
        result = count_lead_letter('this is totally a testy test')
        assert result['i'] == 1


class TestExercise4(unittest.TestCase):
    def test_1(self):
        result = good_movies(90)
        assert len(result) == 12

    def test_2(self):
        result = good_movies(90)
        assert 'Silver Linings Playbook' in result
    
    def test_3(self):
        result = good_movies(90)
        assert 'The King of Comedy' in result

    def test_4(self):
        result = good_movies(90)
        assert 'Once Upon a Time in America' not in result