import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper_method(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper_method(self):
        self.assertTrue('FOO'.isupper())

    def test_contains(self):
        s = 'Ali is doctor'
        self.assertIn('Ali', s)
        self.assertIn('doctor', s)


# def test_sum_method():
#     assert sum([1, 2, 3]) == 6
#
#
# def test_upper_method():
#     assert 'foo'.upper() == 'FOO'
#     assert 'abc'.upper() == 'ABC'
#

if __name__ == '__main__':
    # test_upper_method()
    # test_sum_method()
    unittest.main(verbosity=2)
    print('Everything is ok')