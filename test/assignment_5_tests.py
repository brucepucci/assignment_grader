import unittest

class TestExercise1(unittest.TestCase):
    def test_1(self):
        assert calc_paycheck(40, 10.) == 400

    def test_2(self):
        assert calc_paycheck(41, 10.) == 410
    
    def test_3(self):
        assert calc_paycheck(41, 10., ot=True) == 415
    
    def test_4(self):
        assert calc_paycheck(0, 10.) == 0
    
    def test_5(self):
        assert calc_paycheck(80, 20., ot=True) == 2000


class TestExercise2(unittest.TestCase):
    def test_1(self):
        assert better_deal(2000, 40, 10) == 'lump sum'

    def test_2(self):
        assert better_deal(200, 40, 10) == 'hourly wage'
    
    def test_3(self):
        assert better_deal(412, 41, 10) == 'lump sum'
    
    def test_4(self):
        assert better_deal(412, 41, 10, True) == 'hourly wage'


class TestExercise3(unittest.TestCase):
    def test_1(self):
        assert calc_distance((0, 0), (0, 1)) == 1

    def test_2(self):
        assert calc_distance((0, 0), (0, 0)) == 0
    
    def test_3(self):
        assert calc_distance((0, 0), (0, -1)) == 1
    
    def test_4(self):
        assert calc_distance((3, 2), (9, 7)) == 61**.5


class TestExercise4(unittest.TestCase):
    def test_1(self):
        assert closest_city('Tokyo') == 'New York'

    def test_2(self):
        assert closest_city('Toronto') == 'New York'
    
    def test_3(self):
        assert closest_city('Hong Kong') == 'Paris'
